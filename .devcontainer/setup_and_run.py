import os
import subprocess
import sys

VENV_DIR = ".venv"
APP_FILE = "streamlit_app.py"
PORT = "8501"
URL = f"http://localhost:{PORT}"

def run(cmd, env=None, shell=False):
    print(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    subprocess.check_call(cmd, env=env, shell=shell)

# 1. Create virtual environment if it doesn't exist
if not os.path.isdir(VENV_DIR):
    run([sys.executable, "-m", "venv", VENV_DIR])

# 2. Prepare environment variables for venv
venv_python = os.path.join(VENV_DIR, "bin", "python")
venv_pip = os.path.join(VENV_DIR, "bin", "pip")
venv_streamlit = os.path.join(VENV_DIR, "bin", "streamlit")

# 3. Install dependencies
run([venv_pip, "install", "--upgrade", "pip"])
run([venv_pip, "install", "streamlit", "openai"])

# 4. Run the Streamlit app
streamlit_proc = subprocess.Popen([venv_streamlit, "run", APP_FILE])

# 5. Open the app in the host's default browser
try:
    # Use shell=True so $BROWSER is expanded
    run(f'$BROWSER {URL}', env=os.environ, shell=True)
except Exception as e:
    print(f"Could not open browser: {e}")

# 6. Wait for Streamlit app to finish
streamlit_proc.wait()
