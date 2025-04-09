import streamlit as st
import os
from dotenv import load_dotenv
import time

# LangChain & related
from langchain_groq import ChatGroq
from langchain_cohere import CohereEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_objectbox.vectorstores import ObjectBox
from langchain.memory import ConversationBufferMemory

# Load API keys
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['COHERE_API_KEY'] = os.getenv('COHERE_API_KEY')

# Streamlit page config
st.set_page_config(page_title="📚 LLaMA 3 RAG Chatbot", layout="wide")
st.title("🧠 LLaMA 3 RAG Chatbot with ObjectBox & Memory")

# Initialize session state
for key in ["chat_history", "vectors", "embeddings", "memory"]:
    if key not in st.session_state:
        if key == "chat_history":
            st.session_state[key] = []
        elif key == "memory":
            st.session_state[key] = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
            )
        else:
            st.session_state[key] = None

# Embedding logic
def vector_embedding():
    st.session_state.embeddings = CohereEmbeddings()
    loader = PyPDFDirectoryLoader('./us_census')  # Change folder if needed
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)

    st.session_state.vectors = ObjectBox.from_documents(
        split_docs,
        st.session_state.embeddings,
        embedding_dimensions=768
    )
    st.success("✅ Documents embedded successfully!")

# Auto-load & embed docs once on app start
if st.session_state.vectors is None:
    with st.spinner("🔄 Loading and embedding documents..."):
        vector_embedding()

# Chat input & answer logic
sources = []  # Always define to avoid NameError
user_input = st.chat_input("Ask a question about the documents...")

if user_input and st.session_state.vectors:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    llm = ChatGroq(model='llama-3.3-70b-versatile')
    retriever = st.session_state.vectors.as_retriever()

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        memory=None  # manual memory handling
    )

    # Run chain & track time
    start = time.process_time()
    result = qa_chain.invoke({
        "question": user_input,
        "chat_history": st.session_state.memory.chat_memory.messages
    })
    elapsed = time.process_time() - start

    # Save only the "answer" in memory to avoid LangChain error
    st.session_state.memory.save_context(
        {"input": user_input},
        {"output": result["answer"]}
    )

    st.session_state.chat_history.append({"role": "assistant", "content": result["answer"]})
    sources = result.get("source_documents", [])

# Render chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Render retrieved document chunks
if user_input and sources:
    with st.expander("🔍 Retrieved Document Chunks"):
        for i, doc in enumerate(sources):
            st.markdown(f"**Chunk {i+1}:**\n\n{doc.page_content}")
            st.markdown("---")
