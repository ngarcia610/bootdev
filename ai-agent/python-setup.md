uv init --no-package myagent
cd myagent
uv venv
source .venv/bin/activate
uv add openai==2.44.0
uv add python-dotenv==1.1.0
uv run main.py
