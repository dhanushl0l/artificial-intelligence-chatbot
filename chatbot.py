import os
import json
from fuzzywuzzy import process
import spacy

print("Chatbot")
print("type 'stop' to exit")

current_directory = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(current_directory, "data.json")

try:
    with open(FILE_NAME, "r") as file:
        pairs = json.load(file)
except FileNotFoundError:
    pairs = []

nlp = spacy.load("en_core_web_sm")

print("Chatbot: Hello! How can I assist you today?")
user_name = None

while True:
    user_input = input("You: ")

    if user_input.lower() == "stop":
        print("Chatbot: Goodbye! Have a great day!")
        break

    if user_name is None and user_input.lower().startswith("my name is "):
        user_name = user_input[11:]
        print(f"Chatbot: Nice to meet you, {user_name}!")
    else:
        doc = nlp(user_input)
        preprocessed_input = " ".join([token.lemma_ for token in doc if token.is_alpha])
        best_match_score = 0
        best_response = None

        for pattern, responses in pairs:
            pattern_doc = nlp(pattern)
            processed_pattern = " ".join([token.lemma_ for token in pattern_doc if token.is_alpha])
            match, score = process.extractOne(preprocessed_input, [processed_pattern])
            if score > best_match_score:
                best_match_score = score
                best_response = responses[0]

        if best_match_score < 70:
            response = "I'm sorry, I didn't understand that. Can you please rephrase your question or provide more details?"
            new_response = input("Chatbot: " + response + " Please provide a response for the previous input: ")

            if new_response.lower() == "stop":
                print("Chatbot: Input skipped. How can I assist you further?")
                continue

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
