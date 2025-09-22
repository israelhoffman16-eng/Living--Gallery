#!/bin/bash
# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install streamlit openai

# Run the Streamlit app
streamlit run streamlit_app.py

# Open the app in the host's default browser
"$BROWSER" http://localhost:8501
