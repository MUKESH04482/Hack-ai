from google.adk.agents import Agent
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Create your Research Assistant Agent
root_agent = Agent(
    model='gemini-2.5-pro',

    name="research_assistant",

    description="AI Research Assistant that summarizes content, extracts key points, and provides insights.",

    instruction="""
You are a high-level Research Assistant.

Tasks:
1. Summarize clearly
2. Extract key points
3. Provide insights

Rules:
- Be structured
- Use bullet points
- Be concise
- If input is small, answer directly
"""
)