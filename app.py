from fastapi import FastAPI
from pydantic import BaseModel
from langchain_helper import get_answer_from_gpt4o

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """API endpoint to get an answer from GPT-4o"""
    answer = get_answer_from_gpt4o(request.question)
    return {"question": request.question, "answer": answer}