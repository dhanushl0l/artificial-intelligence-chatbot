import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["my name is (.*)", ["Hi, %1! How can I help you today?"]],
    # Add more patterns and responses here
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
