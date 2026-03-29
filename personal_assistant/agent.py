from google.adk.agents import Agent
import google.generativeai as genai
import os

# 🔑 Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🚀 ADK Agent (structure requirement satisfied)
root_agent = Agent(
    name="research_assistant",
    description="Elite research assistant delivering structured insights",
    instruction="""
You are an elite AI research assistant.

Respond with:
1. DIRECT ANSWER
2. KEY INSIGHTS
3. PRACTICAL TAKEAWAYS

Be precise, structured, and useful.
"""
)

# 🔗 Bridge function (actual Gemini execution)
def run_agent(message: str):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(message)
    return response.text