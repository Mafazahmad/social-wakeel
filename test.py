from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

def getlaw(question):
    url = "http://traverser25.pythonanywhere.com/getlaw"
    data = {"question": question}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        reply = response.json()["response"]
        return reply
    else:
        return "Failed to generate reply. Status code: {}".format(response.status_code)

@app.route("/")
def home():
    # Mock data for index page
    mock_chats = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "How tall is Mount Everest?", "answer": "8848 meters"},
        {"question": "What is the boiling point of water?", "answer": "100 degrees Celsius"}
    ]
    return render_template("index.html", myChats=mock_chats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        response = getlaw(question)
        data = {"question": question, "answer": response}
        return jsonify(data)
    
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
