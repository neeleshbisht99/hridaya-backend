from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = "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"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific origins
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    title: str
    description: str
    ai_advice: str = ""
    done: bool

class Conversation(BaseModel):
    text: str

tasks = []

@app.get("/tasks/")
async def read_tasks():
    return tasks


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
