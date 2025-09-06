from langchain_groq import ChatGroq
import os

def get_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.5,
        max_tokens=1024
    )