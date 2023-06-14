from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['OPENAI_API_KEY']
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific origins
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Conversation(BaseModel):
    text: str

@app.get("/")
async def home():
    return {"message": "Hello World"}


@app.post("/chat/")
async def converse(conversation:Conversation):
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      temperature = 0.2,
      max_tokens = 3000,
      messages = [
        {"role": "user", "content": conversation.text}
      ]
    )
    return response
