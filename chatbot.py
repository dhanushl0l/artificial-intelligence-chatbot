import os
import re
import json
from fuzzywuzzy import process
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

current_directory = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(current_directory, "data.json")

try:
    with open(FILE_NAME, "r") as file:
        pairs = json.load(file)
except FileNotFoundError:
    pairs = []

def save_data(pairs):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(pairs, file)
    except Exception as e:
        print(f"Error occurred while saving data: {e}")

def get_chatbot_response(user_input):
    preprocessed_input = re.sub(r'[^\w\s]', '', user_input).lower()
    best_match_score = 0
    best_response = None

    for pattern, responses in pairs:
        match, score = process.extractOne(preprocessed_input, [pattern])
        if score > best_match_score:
            best_match_score = score
            best_response = responses[0]

    if best_match_score < 95:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question or provide more details?"
    else:
        return best_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.get_json()['user_input']
    chatbot_response = get_chatbot_response(user_input)

    # If the match score is below 95, set a flag to indicate that user input is required
    response_data = {'response': chatbot_response, 'input_required': False}

    if chatbot_response == "I'm sorry, I didn't understand that. Can you please rephrase your question or provide more details?":
        response_data['input_required'] = True

    # Add user input and chatbot response to pairs
    pairs.append([user_input, [chatbot_response]])
    save_data(pairs)

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
