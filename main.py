import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from groq import Groq
from pydantic import BaseModel

from toolhouse_helper import get_real_context

# Load environment variables from .env file
load_dotenv()
app = FastAPI()

# Load Groq API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class AgentObject(BaseModel):
    name: str
    type: str
    description: str
    isReal: bool

@app.post("/chatWithGroq", response_model=ChatResponse)
async def chat_with_groq(request: ChatRequest):
    try:
        client = Groq(api_key=GROQ_API_KEY)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initializing Groq client: {str(e)}")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="llama3-8b-8192",
        )

        # Extract the content from the response
        response_content = chat_completion.choices[0].message.content
        return ChatResponse(response=response_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Groq: {str(e)}")

@app.post("/chatWithToolhouse", response_model=ChatResponse)
async def chat_with_toolhouse(request: ChatRequest):
    # This is a placeholder function for chat completion with Toolhouse
    return ChatResponse(response="This is a placeholder response from Toolhouse")

@app.post("/getRealContext", response_model=ChatResponse)
async def get_real_context(request: AgentObject):
    response = await get_real_context(request.dict())
    if response is None:
        raise HTTPException(status_code=500, detail="Error getting real context")
    return ChatResponse(response=response)



@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)