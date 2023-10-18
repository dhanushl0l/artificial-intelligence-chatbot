# Chatbot

This is a simple text-based chatbot created using Python.

## Note
As per the instructions given, the requirement was to utilize a text file as the dataset. However, I chose to use a JSON format due to its superior capability in maintaining structured data integrity. Additionally, utilizing JSON allows me to dynamically add patterns in real-time, enhancing the chatbot's responsiveness and adaptability.
## Features

- Responds to specific patterns in user input.
- Add more patterns and responses as needed.

## Prerequisites

- Python 3.x
- NLTK library

## Video Demo
[![Demo Video](https://www.dsecctv.com/images/Demo%20clip%20icon%20md.png)](https://youtu.be/mJ9Tkuu33Is)

Click the above image to watch the demo video.

## Requirements

    pip install fuzzywuzzy
    pip install nltk

## Usage

Just download the sorce file and run the `chatbot.py` file using python and `data.json` file should in the same folder as the `chatbot.py` file:

## Customization

Users can customize the chatbot's responses by modifying the data.json file. Follow the chatbot's prompts to add new responses during the conversation.

## File Structure

    chatbot.py: Contains the main chatbot logic.
    data.json: Stores the chatbot's conversation pairs.

## License

Anyone can clone and modify this project, which I created for my college project. Feel free to make any changes and submit a pull request.
