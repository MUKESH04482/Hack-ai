# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Import your Gemini agent
from personal_assistant.agent import run_agent


@app.route('/')
def home():
    return "Hack AI is running 🚀"


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message is required"}), 400

        user_input = data["message"]

        # 🔥 Call your AI agent
        response = run_agent(user_input)

        return jsonify({
            "response": response
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)