This is a simple example demonstrating how to create and run an AI assistant agent using **Chainlit** 🤖, **OpenAI Async API** 🚀, and the **openai-agents** SDK 🛠️.

---

## Features ✨

- 🔐 Loads environment variables from `.env`
- 🗝️ Uses OpenRouter API key for authentication
- 🤖 Creates an AI agent with specific instructions
- 🌀 Streams the AI response token-by-token to Chainlit chat UI
- 👥 Maintains agent instance per user session

---

## Prerequisites 📋

- 🐍 Python 3.8+
- 📦 Install dependencies:

```bash
pip install chainlit openai-agents openai python-dotenv
🔑 A valid OpenRouter API key stored in .env file as:

ini
Copy
OPEN_ROUTER_API_KEY=your_api_key_here
How to Run ▶️
📂 Clone this repo or save your script as main.py.

⚙️ Activate your virtual environment (recommended):

bash
Copy
# Windows
.\\.venv\\Scripts\\activate

# macOS/Linux
source .venv/bin/activate
▶️ Run Chainlit app with:

bash
Copy
chainlit run main.py -w
🌐 Open your browser at http://localhost:8000 to interact with the agent.

Code Overview 📝
📥 Loads environment variables via dotenv

🌐 Creates an async OpenAI client with OpenRouter base URL

🧠 Defines an AI Agent with a helpful assistant prompt

🚀 On chat start, the agent instance is stored in user session

💬 On each user message:

📨 A Chainlit message is created and sent immediately with empty content

🔄 The agent runs asynchronously and streams token responses

⚡ Tokens are streamed live to the Chainlit message

✅ Final content updates the message

Notes 🛎️
✔️ Ensure your OpenRouter API key is valid and has sufficient quota

🔧 The msg.update() method is used to finalize the message without arguments

🎯 For streaming token-by-token updates, msg.stream_token() is used

pgsql
Copy
