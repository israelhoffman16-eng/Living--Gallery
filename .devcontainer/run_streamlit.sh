#!/bin/bash

# Set your OpenAI API key here
export OPENAI_API_KEY="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"

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
streamlit run streamlit_app.py &

# Wait a moment for the server to start, then open in browser
sleep 3
"$BROWSER" http://localhost:8501
