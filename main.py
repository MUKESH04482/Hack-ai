import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent

# ── App setup ─────────────────────────────────────────────────────────────────
app = FastAPI(
    title="ADK Gemini Agent API",
    description="A single AI agent built with Google ADK + Gemini, hosted on Render.",
    version="1.0.0",
)

# ── ADK Session + Runner setup ────────────────────────────────────────────────
APP_NAME   = "adk_gemini_agent"
USER_ID    = "render_user"
SESSION_ID = "session_001"

session_service = InMemorySessionService()

# Create session at startup so it always exists
session_service.create_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


# ── Schemas ───────────────────────────────────────────────────────────────────
class AgentRequest(BaseModel):
    message: str

class AgentResponse(BaseModel):
    response: str
    status: str = "success"


# ── Helper ────────────────────────────────────────────────────────────────────
async def run_agent(user_message: str) -> str:
    content = types.Content(
        role="user",
        parts=[types.Part(text=user_message)],
    )

    final_response = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text
            break

    return final_response or "No response generated."


# ── Routes ────────────────────────────────────────────────────────────────────
@app.get("/")
async def health_check():
    return {"status": "healthy", "agent": root_agent.name}


@app.post("/run", response_model=AgentResponse)
async def run_agent_endpoint(request: AgentRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    try:
        response_text = await run_agent(request.message)
        return AgentResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize", response_model=AgentResponse)
async def summarize_endpoint(request: AgentRequest):
    prompt = f"Please summarize the following text:\n\n{request.message}"
    try:
        response_text = await run_agent(prompt)
        return AgentResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/classify", response_model=AgentResponse)
async def classify_endpoint(request: AgentRequest):
    prompt = f"Please classify the following text:\n\n{request.message}"
    try:
        response_text = await run_agent(prompt)
        return AgentResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)