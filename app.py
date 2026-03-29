from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from personal_assistant.agent import run_agent


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message is required"}), 400

        user_input = data["message"]

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