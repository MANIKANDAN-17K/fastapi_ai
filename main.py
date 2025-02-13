from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini AI API
genai.configure(api_key="AIzaSyA0Qi4nXfPnLCSD9HyE9ATJ06Dijpiu5G4")

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(message.text)
    return {"response": response.text}
