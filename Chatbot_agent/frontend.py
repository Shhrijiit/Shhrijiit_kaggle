# Step1: Setup UI with streamlit (model provider, model, system prompt, query)

import streamlit as st
import json

st.set_page_config(page_title = 'LangGraph Agent UI', layout = 'centered')
st.title('AI CHATBOT AGENT')
st.write("Create and Interact with AI Agents!")

system_prompt = st.text_area('Define your AI Agent', height = 70, placeholder = 'Type your system prompt here...')

MODEL_NAMES_GROQ = ['llama-3.3-70b-versatile','mistral-saba-24b']
MODEL_NAMES_GOOGLE = ['gemini-1.5-pro-latest']

provider = st.radio('Select Provider:',("Groq","Google"))

if provider == 'Groq':
    selected_model = st.selectbox('Select Groq Model:', MODEL_NAMES_GROQ)
elif provider == 'Google':
    selected_model = st.selectbox('Select Google Model:', MODEL_NAMES_GOOGLE)

allow_web_search = st.checkbox('Allow Web Search')

user_query = st.text_area('Enter you query:', height = 70, placeholder = 'Ask Anything!')

API_URL = 'http://127.0.0.1:9999/chat'

if st.button('Ask Agent!'):
    if user_query.strip():
        # Step2: Connect with backend via URL

        import requests 
        payload = {
                'model_name': selected_model,
                'model_provider': provider,
                'system_prompt' : system_prompt,
                'messages' :[user_query],
                'allow_search' : allow_web_search
        } 

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

