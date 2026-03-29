from google.adk.agents import Agent
import os

# Ensure API key exists
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("Missing GOOGLE_API_KEY")

# ✅ Proper ADK agent

root_agent = Agent(
    name="research_assistant",   # ✅ REQUIRED
    model="models/gemini-2.5-flash",  # ✅ correct format
    instruction="Give clear and structured answers"
)

def run_agent(message: str):
    try:
        result = root_agent.run(message)   # ✅ THIS is correct for LlmAgent
        return str(result)
    except Exception as e:
        print("AGENT ERROR:", str(e))
        return f"Error: {str(e)}"