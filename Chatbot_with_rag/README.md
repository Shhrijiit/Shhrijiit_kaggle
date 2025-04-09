# 📚 Llama 3 RAG Chatbot with ObjectBox Vector Store

This project demonstrates a **Retrieval-Augmented Generation (RAG)** chatbot built using the latest **LLaMA 3 (70B)** model via **Groq**, combined with **ObjectBox** as a blazing-fast local vector database. The system allows you to ask natural language questions over a collection of PDF documents (like US Census data) and get highly relevant, context-aware answers in real-time.

<div align="center">
  <img src="https://img.shields.io/badge/Built%20With-LangChain-blue" />
  <img src="https://img.shields.io/badge/LLM-LLaMA%203%2070B%20via%20Groq-green" />
  <img src="https://img.shields.io/badge/Embeddings-Cohere-purple" />
  <img src="https://img.shields.io/badge/VectorStore-ObjectBox-orange" />
  <img src="https://img.shields.io/badge/UI-Streamlit-red" />
</div>

---

## 🚀 Features

- 🧠 **RAG Pipeline** with LangChain
- 🦙 **LLaMA 3 (70B)** integration using Groq's blazing-fast inference
- 🧾 PDF ingestion & intelligent chunking
- 📦 Local vector storage with **ObjectBox**
- 🔍 Semantic search & context retrieval
- 🖥️ Simple, interactive UI with **Streamlit**

---

## 🛠️ Tech Stack

| Component     | Description                               |
|---------------|-------------------------------------------|
| 🦜 LangChain   | Framework for chaining LLM and retrievers |
| 🦙 LLaMA 3      | Open-source large language model from Meta |
| ⚡ Groq        | Fast inference engine for LLMs            |
| 🧠 Cohere     | Embedding model for vector similarity     |
| 📦 ObjectBox  | Lightweight vector database               |
| 🧾 PyPDFLoader | Extracts text from PDFs                   |
| 🎛️ Streamlit  | Frontend for interaction                  |

---

## 📂 Directory Structure

📁 your-project/ │ ├── 📄 app.py # Main Streamlit app ├── 📁 us_census/ # Folder containing PDF documents ├── 📄 .env # API keys └── 📄 requirements.txt # Python dependencies

## 🌟 Acknowledgments

- LangChain
- Meta AI - LLaMA 3
- Groq
- Cohere
- ObjectBox Vector DB


