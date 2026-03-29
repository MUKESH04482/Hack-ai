from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

from personal_assistant.agent import run_agent


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    # 🔥 NO try-except (we want real error)
    response = run_agent(user_input)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)