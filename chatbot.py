import os
import nltk
import re
from fuzzywuzzy import process 
from nltk.chat.util import Chat, reflections

FILE_NAME = "chatbot_data.txt"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        pairs = eval(file.read())

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")

    if user_input.lower() == "stop":
        print("Chatbot: Goodbye! Have a great day!")
        break

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
        
        pairs.append([preprocessed_input, [new_response]])
        
        with open(FILE_NAME, "w") as file:
            file.write(str(pairs))
        
        response = "Thanks! I've added that response. How can I assist you further?"
    else:
        response = best_response
    
    print("Chatbot:", response)
