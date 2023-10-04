import nltk
import re
from nltk.chat.util import Chat, reflections

pairs = [
    [r"my name is (.*)", ["Hi, %1! How can I help you today?"]],
    [r"what is your name", ["I am just a chatbot. You can call me whatever you like!"]],
    [r"(.*)my name is (.*)", ["Hi, %2! How can I help you today?"]],
    # Add more patterns and responses here
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")

    preprocessed_input = re.sub(r'[^\w\s]', '', user_input).lower()

    response = chatbot.respond(preprocessed_input)
    print("Chatbot:", response)
