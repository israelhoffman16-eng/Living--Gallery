# === Quick Start ===
# To run this app in the dev container, use:
#   ./run_streamlit.sh
# ====================
# After the app starts, open it in your host's default browser with:
#   "$BROWSER" http://localhost:8501

import streamlit as st
import openai
import os

# Make sure your OpenAI API key is set in your environment
# e.g. export OPENAI_API_KEY="your_key_here"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Image generator using OpenAI DALL·E
def generate_image(prompt):
    try:
        response = openai.images.generate(
            model="dall-e-3",  # Use the correct DALL·E model name
            prompt=prompt,
            size="512x512"
        )
        return response.data[0].url
    except Exception as e:
        st.error(f"Image generation failed: {e}")
        return None

# Keep track of 3 paintings
if "paintings" not in st.session_state:
    st.session_state.paintings = [None, None, None]
    st.session_state.prompts = ["", "", ""]
    st.session_state.index = 0  # Which slot to replace next

st.title("🎨 AI Painting Wall")

# Display current images
cols = st.columns(3)
for i in range(3):
    if st.session_state.paintings[i]:
        cols[i].image(st.session_state.paintings[i], caption=st.session_state.prompts[i])
    else:
        cols[i].write("(empty)")

st.subheader("Create or Modify a Painting")

# Prompt input
prompt = st.text_area("Enter a description (or modify an old one):")

# Dropdown to reuse/modify a previous prompt
modify_choice = st.selectbox(
    "Or pick a previous prompt to edit:",
    ["None"] + [p for p in st.session_state.prompts if p]
)

if modify_choice != "None" and not prompt:
    prompt = modify_choice

if st.button("Generate Painting") and prompt:
    new_img = generate_image(prompt)
    if new_img:
        idx = st.session_state.index
        st.session_state.paintings[idx] = new_img
        st.session_state.prompts[idx] = prompt
        st.session_state.index = (idx + 1) % 3  # Cycle replacement
        st.experimental_rerun()
