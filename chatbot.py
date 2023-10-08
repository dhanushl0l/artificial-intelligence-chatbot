import os
import re
import json
from fuzzywuzzy import process 
from nltk.chat.util import Chat, reflections

FILE_NAME = "chatbot_data.json"

try:
    with open(FILE_NAME, "r") as file:
        pairs = json.load(file)
except FileNotFoundError:
    pairs = []  

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! How can I assist you today?")
user_name = None  
preprocessed_input = None  
best_match_score = 0  

while True:
    user_input = input("You: ")

    if user_input.lower() == "stop":
        print("Chatbot: Goodbye! Have a great day!")
        break

    if user_name is None and re.match(r'my name is (.+)', user_input, re.IGNORECASE):
        user_name = re.match(r'my name is (.+)', user_input, re.IGNORECASE).group(1)
        print(f"Chatbot: Nice to meet you, {user_name}!")
    else:
        preprocessed_input = re.sub(r'[^\w\s]', '', user_input).lower()
        best_match_score = 0  
        best_response = None  

        for pattern, responses in pairs:
            match, score = process.extractOne(preprocessed_input, [pattern])
            if score > best_match_score:
                best_match_score = score
                best_response = responses[0]

        if best_match_score < 80:
            response = "I'm sorry, I didn't understand that. Can you please rephrase your question or provide more details?"
        
            new_response = input("Chatbot: " + response + " Please provide a response for the previous input: ")

            # Prevent adding duplicate entries
            new_entry = [preprocessed_input, [new_response]]
            if new_entry not in pairs:
                pairs.append(new_entry)

            try:
                with open(FILE_NAME, "w") as file:
                    json.dump(pairs, file)
            except Exception as e:
                print(f"Error occurred while saving data: {e}")

            print("Chatbot: Thanks! I've added that response. How can I assist you further?")
        else:
            print("Chatbot:", best_response)

