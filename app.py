from flask import Flask, render_template, request, jsonify
import random
import json
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Load the intents data from data.json
with open('data.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

def get_bot_response(user_message):
    user_message = user_message.lower()
    matching_intents = []

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            similarity = fuzz.partial_ratio(user_message, pattern.lower())
            if similarity > 70:  # Adjust the threshold as needed
                matching_intents.append(intent)

    if matching_intents:
        selected_intent = random.choice(matching_intents)
        return random.choice(selected_intent.get('responses', ["Je ne comprends pas la réponse pour cette intention."]))
    else:
        return "Je m'excuse, je ne comprends pas. Pouvez-vous reformuler votre question ?"

def is_greeting(user_message):
    greetings = ['bonjour', 'salut', 'hello', 'hi']
    return any(greeting in user_message for greeting in greetings)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    
    if is_greeting(user_message):
        return jsonify({'bot_message': "Bonjour ! Comment puis-je vous aider aujourd'hui ?"})
    
    bot_message = get_bot_response(user_message)
    return jsonify({'bot_message': bot_message})

if __name__ == '__main__':
    app.run(debug=True, port=5018)
