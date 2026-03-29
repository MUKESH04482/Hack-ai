from google.adk.agents import LlmAgent
import os

# Ensure API key exists
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("Missing GEMINI_API_KEY")

# ✅ Proper ADK agent
root_agent = LlmAgent(
    model="gemini-2.5-flash",
    instruction="Give clear and structured answers"
)

def run_agent(message: str):
    try:
        result = root_agent.run(message)   # ✅ THIS is correct for LlmAgent
        return str(result)
    except Exception as e:
        print("AGENT ERROR:", str(e))
        return f"Error: {str(e)}"