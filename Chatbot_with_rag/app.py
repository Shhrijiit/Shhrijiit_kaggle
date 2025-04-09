import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_cohere import CohereEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_objectbox.vectorstores import ObjectBox
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['COHERE_API_KEY'] = os.getenv('COHERE_API_KEY')

st.title('ObjectBox VectorStoreDB with Llama3 Demo')

llm = ChatGroq(model = 'llama-3.3-70b-versatile')

prompt = ChatPromptTemplate.from_template(
"""
 Answer the questions on provided context only. 
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}
"""
)

#Vector Embedding and Object VectorStore DB

def vector_embedding():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings = CohereEmbeddings()
        st.session_state.loader = PyPDFDirectoryLoader('./us_census')
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                                                        chunk_overlap = 200)
        st.session_state.final_docs = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = ObjectBox.from_documents(st.session_state.final_docs,st.session_state.embeddings,embedding_dimensions = 768)

input_prompt = st.text_input('Enter your questions from the documents')

if st.button('Document_embeddings'):
    vector_embedding()
    st.write('ObjectBox DB is ready!')

import time

if input_prompt:
    document_chain = create_stuff_documents_chain(llm,prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever,document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input':input_prompt})

    print('Response Time:', time.process_time()-start)
    st.write(response['answer'])

    #with a streamlit expander
    with st.expander("Document Similarity search"):
        #find relavant chunks
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("-----------------------------------")
