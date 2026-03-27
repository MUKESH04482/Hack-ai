from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/api")
def home():
    return jsonify({"status": "WORKING 🚀"})