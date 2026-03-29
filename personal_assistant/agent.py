from google.adk.agents import Agent
import os

# ADK automatically uses Gemini via API key
# Just ensure GEMINI_API_KEY is set in Render

root_agent = Agent(
    name="research_assistant",
    description="Elite research assistant delivering precise, structured insights",
    instruction="""
You are an elite AI research assistant.

Give:
1. Direct Answer
2. Key Insights
3. Practical Takeaways

Be concise and precise.
"""
)

def run_agent(message: str):
    response = root_agent.run(message)
    return str(response)