#1. Setup API keys for Groq and Tavily
import os


GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

#2. Setup & Tools
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

#3. Setup AI Agent with Search Tool functionality
 
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage 
system_prompt = 'Act as an AI Chatbot who is smart and friendly'

def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider =='Groq':
        llm = ChatGroq(model = llm_id)
    elif provider=="Google":
        llm=ChatGoogleGenerativeAI(model=llm_id)

    tools = [TavilySearchResults(max_results = 2)] if allow_search else []


    agent = create_react_agent(
    model = llm,
    tools = tools,
    state_modifier = system_prompt
    )


    state = {'messages':query}
    response = agent.invoke(state)
    messages = response.get('messages')
    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]
    return ai_messages[-1]
    