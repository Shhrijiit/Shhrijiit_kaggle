# 🧠 AI Chatbot Agent UI

An interactive AI chatbot interface built with **Streamlit** (Frontend) and **FastAPI** (Backend), capable of connecting to multiple AI model providers like **Groq** and **Google**.

This project allows users to define custom system prompts, choose model providers, and optionally enable web search. Designed for simplicity, speed, and flexibility.

---

## 🚀 Features

- 🔌 Connects with AI models from Groq and Google
- 💬 Send user queries with custom system prompts
- 🌐 Optional web search integration
- ⚙️ Modular backend using FastAPI
- 🖼️ Clean and simple frontend using Streamlit

---

## 🗂️ Project Structure
.
├── frontend.py      # Streamlit UI
├── backend.py       # FastAPI server
├── ai_agent.py      # AI agent logic
├── README.md        # You’re reading it!

📌 Notes
Make sure your local API is running before using the frontend

API URL: http://127.0.0.1:9999/chat


🙌 Acknowledgements
LangGraph for ReAct Agents
FastAPI for API Calls
Streamlit for UI (Frontend)
Groq, Google, Gemini for LLM
LangChain for tools
Uvicorn for hosting the App
Python
Pydantic
Tavily
VS Code
