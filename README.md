# Mini-Agent-with-Local-Chained-Tasks
An open-source, lightweight AI agent that takes any goal, breaks it into 3 actionable subtasks, and explains the reasoning behind each—powered **locally** using Mistral via Ollama, LangChain, and Python.

# 🧠 Mini Agent with Local Chained Tasks

An open-source, lightweight AI agent that takes any goal, breaks it into 3 actionable subtasks, and explains the reasoning behind each—powered **locally** using Mistral via Ollama, LangChain, and Python.

---

## 🔍 What It Does
- Accepts a **high-level goal** from the user
- Decomposes it into a **3-step plan**
- Provides **brief reasoning** for each step
- Runs on a **local LLM** using [Ollama](https://ollama.com/)
- Has a simple and clean **Gradio-based interface**

---
## 🚀 Demo
<img width="945" alt="res1" src="https://github.com/user-attachments/assets/b59901ef-b323-414d-ba90-b11a01bd4f44" />

> Example: _"I want to get a job as a data analyst in 3 months."_  
→ Returns a practical 3-step plan with context.

---

## 🧰 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) with `mistral` model
- [Gradio](https://www.gradio.app/)
- Python 3.9+

---

## 🛠️ Installation

## 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mini-agent-chained-tasks.git
cd mini-agent-chained-tasks
```

2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Start Ollama
```bash
ollama run mistral
```

5. Run the App
```bash
python app.py
```

Then open your browser at http://localhost:7860

🧪 Example Prompts
"I want to start a YouTube channel about tech tutorials."
"I want to learn Python for data science."
"I want to build a portfolio website to showcase my projects."

📁 Project Structure
```graphql
.
├── app.py              # Gradio frontend
├── agent_runner.py     # LangChain + local LLM agent logic
├── requirements.txt    # Python dependencies
└── README.md
```

💡 Inspiration
Inspired by LangChain agents and task decomposition workflows, this project is part of my #30DaysOfGenAI challenge.

🧠 What I Learned
How to chain reasoning tasks using LangChain
How to use local LLMs with zero API calls
How to deploy a local AI app with a clean UI using Gradio

🌐 Connect
Made with 💻 and ☕ by Varshitha Yanamala






