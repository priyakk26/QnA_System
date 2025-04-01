from langchain_openai import ChatOpenAI
from database import fetch_qna
import os
from dotenv import load_dotenv

load_dotenv()  # Load API Key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_answer_from_gpt4o(user_query):
    """Use GPT-4o to generate an answer"""
    qna_data = fetch_qna()
    
    # Create a knowledge base from stored QnA
    knowledge_base = "\n".join([f"Q: {q['question']}\nA: {q['answer']}" for q in qna_data])
    
    prompt = f"""
    You are a helpful assistant. Answer the question based on the given knowledge base.
    
    Knowledge Base:
    {knowledge_base}
    
    User Question: {user_query}
    Answer:
    """
    
    llm = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)
    response = llm.invoke(prompt)
    return response.content.strip()