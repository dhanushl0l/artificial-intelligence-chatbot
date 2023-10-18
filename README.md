# Chatbot

This is a simple text-based chatbot created using Python.

## Note
As per the instructions given, the requirement was to utilize a text file as the dataset. However, I chose to use a JSON format due to its superior capability in maintaining structured data integrity. Additionally, utilizing JSON allows me to dynamically add patterns in real-time, enhancing the chatbot's responsiveness and adaptability.

To convert text-based datasets into JSON format just use [this py program](https://github.com/dhanushl0l/TxtToJsonConverter).
## Features

- Responds to specific patterns in user input.
- Add more patterns and responses as needed.

## Prerequisites

- Python 3.x
- NLTK library
- fuzzywuzzy library

## Demo
<img src="https://camo.githubusercontent.com/a39e6274c6e8090a657fa8d5d803b9a6f0ec4b783c428aaf5b38bcc231cbff3a/68747470733a2f2f696d322e657a6769662e636f6d2f746d702f657a6769662d322d643936633331303736312e676966" alt="browser history output" style="max-width:70%;box-shadow:0 2.8px 2.2px rgba(0, 0, 0, 0.12)">

## Usage

Just download the sorce file and run the `chatbot.py` file using python and `data.json` file should in the same folder as the `chatbot.py` file:

## Customization

Users can customize the chatbot's responses by modifying the data.json file. Follow the chatbot's prompts to add new responses during the conversation.

## File Structure

    chatbot.py: Contains the main chatbot logic.
    data.json: Stores the chatbot's conversation pairs.

## License

Anyone can clone and modify this project, which I created for my college project. Feel free to make any changes and submit a pull request.
