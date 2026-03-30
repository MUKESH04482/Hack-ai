import os
from google.adk.agents import Agent

# Load API key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set!")
# Define a simple tool for the agent
def summarize_text(text: str) -> dict:
    """
    Summarizes the given text.
    Args:
        text: The text to summarize.
    Returns:
        A dictionary with the summary result.
    """
    return {"action": "summarize", "input": text}
 
 
def answer_question(question: str, context: str = "") -> dict:
    """
    Answers a question, optionally using provided context.
    Args:
        question: The question to answer.
        context: Optional context to help answer the question.
    Returns:
        A dictionary with the question and context.
    """
    return {"action": "answer", "question": question, "context": context}
 
 
def classify_text(text: str) -> dict:
    """
    Classifies the intent or category of the given text.
    Args:
        text: The text to classify.
    Returns:
        A dictionary with the classification input.
    """
    return {"action": "classify", "input": text}
 
 
# Create the ADK Agent using Gemini
root_agent = Agent(
    name="gemini_assistant",
    model="gemini-2.0-flash",          # Gemini model for inference
    description=(
        "A helpful AI assistant that can summarize text, "
        "answer questions, and classify input text."
    ),
    instruction=(
        "You are a helpful assistant. When the user asks you to summarize, "
        "use the summarize_text tool. When asked a question, use answer_question. "
        "When asked to classify text, use classify_text. "
        "Always be concise and accurate."
    ),
    tools=[summarize_text, answer_question, classify_text],
)