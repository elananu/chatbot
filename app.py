# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Extended chatbot logic with more responses
def generate_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking! How can I help you?"
    elif "what is your name" in user_input:
        return "I'm your friendly chatbot created to assist you."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I'm here to assist you with basic queries. You can ask me about my functionality or just chat!"
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    elif "thank you" in user_input:
        return "You're welcome! Feel free to ask anything else."
    elif "joke" in user_input:
        return "Why don't programmers like nature? It has too many bugs!"
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase your question?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
