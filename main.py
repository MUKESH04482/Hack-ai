from fastapi import FastAPI
from pydantic import BaseModel
from personal_assistant.agent import root_agent

app = FastAPI()

# Request format
class Query(BaseModel):
    question: str

# Health check
@app.get("/")
def home():
    return {"status": "Research Assistant API is running"}

# Main AI endpoint
@app.post("/ask")
def ask(query: Query):
    try:
        response = root_agent.run(query.question)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}