# Step 1: Setup Pydantic model (Schema Validation)

from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):

    model_name: str
    model_provider: str
    system_prompt : str
    messages :List[str]
    allow_search : bool


#Step 2: Setup AI Agent from Frontend Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "mistral-saba-24b", "llama-3.3-70b-versatile", "gemini-1.5-pro-latest"]

app = FastAPI(title = 'LanGraph AI Agent')

@app.post('/chat')
def chat_endpoint(request: RequestState):
   """
   API Endpoint to interact with the Chatbot using LangGraph and search tools.
   It dynamically selects the model specidied in thee request
   """
   if request.model_name not in ALLOWED_MODEL_NAMES:
       return {'error':'Invalid Model Name. Kindly select a valid AI Model'}
   
   llm_id = request.model_name
   query = request.messages
   allow_search =request.allow_search
   system_prompt = request.system_prompt
   provider=request.model_provider

   #Create AI Agent and get response from it!
   response = get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)

   return response


#Step 3: Runn App & Explore Swagger UI docs

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port = 9999)