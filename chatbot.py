import nltk
import re
from nltk.chat.util import Chat, reflections

pairs = [
    [r"my name is (.*)", ["Hi, %1! How can I help you today?"]],
    [r"what is your name", ["I am just a chatbot. You can call me whatever you like!"]],
    [r"(.*)my name is (.*)", ["Hi, %2! How can I help you today?"]],
    [r"hello|hi|hey", ["Hello! How can I assist you today?"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!"]],
    [r"what can you do", ["I can help answer your questions and provide assistance. Ask me anything!"]],
    [r"thank you|thanks", ["You're welcome! If you have any more questions, feel free to ask."]],
    [r"(.*)help(.*)", ["Sure, I can assist you with various topics. Please specify what you need help with."]],
    [r"(.*)your age", ["I don't have an age. I'm just a computer program designed to assist you!"]],
    [r"(.*)love(.*)", ["I'm just a chatbot, so I don't experience emotions, but I'm here to help you!"]],
    [r"(.*)weather(.*)", ["I'm sorry, I don't have access to real-time weather information."]],
    [r"(.*)joke(.*)", ["Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"]],
    [r"tell me about yourself", ["I am a chatbot designed to assist and provide information."]],
    [r"how can I contact support", ["For support, visit https://github.com/dhanushl0l."]],
    [r"what is the meaning of life", ["The meaning of life is a philosophical question. It can vary for each individual."]],
    [r"who is your creator", ["I was created by a team of developers passionate about artificial intelligence."]],
    [r"(.*)favorite color(.*)", ["I don't have a favorite color. I'm just a program!"]],
    [r"(.*)favorite food(.*)", ["I don't eat, so I don't have a favorite food."]],
    [r"what is the capital of (.*)", ["The capital of %1 is ... (Sorry, I don't know that one, you can Google it!)"]],
    [r"how do I reset my password", ["To reset your password, visit the login page and click on 'Forgot Password'."]],
    [r"tell me a fun fact", ["Sure, here's a fun fact: Honey never spoils!"]],
    [r"what is the time", ["I'm sorry, I don't have real-time information. Please check your device's clock."]],
    [r"(.*)age(.*)", ["I don't have an age. I'm a computer program."]],
    [r"what do you think about (.*)", ["I don't have opinions. I'm here to provide information and assist you."]],
    [r"can you help me with my homework", ["I can certainly try! Please provide the details of your homework question."]],
    [r"who won the last world series", ["I'm sorry, I don't have real-time sports information. You can check the latest news for updates."]],
    [r"(.*)tell me a story(.*)", ["Once upon a time, in a land far, far away... (Sorry, I'm not very good at storytelling!)"]],
    [r"what is the square root of (.*)", ["The square root of %1 is approximately %.2f."]],
    [r"what is your purpose", ["My purpose is to assist and provide information to the best of my abilities."]],
    [r"how do I learn programming", ["Learning programming can be achieved through online courses, tutorials, and practice. There are many resources available to get started."]],
    [r"what is the population of (.*)", ["I'm sorry, I don't have real-time population data. You can check reliable sources like World Bank or United Nations for the latest population figures."]],
    [r"(.*)tell me a programming joke(.*)", ["Sure, here's one: Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!"]],
    [r"what is the meaning of (.*)", ["The meaning of %1 can vary based on context. Could you provide more details?"]],
    [r"how do I stay motivated", ["Staying motivated involves setting goals, staying positive, and finding your passion. Surround yourself with supportive people and take breaks when needed."]],
    [r"what is the latest technology news", ["For the latest technology news, I recommend visiting reputable tech news websites such as TechCrunch, Wired, or The Verge."]],
    [r"(.*)tell me a science fact(.*)", ["Certainly! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]],
    [r"what is the fastest animal", ["The fastest animal on land is the cheetah, which can reach speeds of up to 75 miles per hour (120 kilometers per hour) in short bursts covering distances up to 500 meters."]],
    [r"what is the tallest mountain", ["The tallest mountain in the world, measured from base to summit, is Mauna Kea in Hawaii. However, if we consider mountains above sea level, Mount Everest in Nepal is the tallest."]],
    [r"(.*)what is your favorite book(.*)", ["I don't have preferences as I am just a computer program. But many people enjoy 'To Kill a Mockingbird' by Harper Lee or '1984' by George Orwell."]],
    [r"how do I improve my communication skills", ["Improving communication skills involves active listening, practicing empathy, and working on clarity in expression. Consider taking communication courses or joining public speaking clubs like Toastmasters."]],
    [r"(.*)tell me a historical fact(.*)", ["Certainly! Did you know that the Great Wall of China is the longest wall in the world, with a total length of approximately 13,170 miles (21,196 kilometers)?"]],
    [r"what is the largest planet in our solar system", ["The largest planet in our solar system is Jupiter."]],
    [r"what is the smallest planet in our solar system", ["The smallest planet in our solar system is Mercury."]],
    [r"how do I start a small business", ["Starting a small business involves creating a business plan, securing financing, and registering your business. It's important to conduct market research and have a clear understanding of your target audience."]],
    [r"(.*)recommend a movie(.*)", ["Certainly! If you enjoy science fiction, I recommend 'Inception' directed by Christopher Nolan. It's a mind-bending film that explores the concept of dreams within dreams."]],
    [r"(.*)your favorite movie(.*)", ["I don't have personal preferences as I am just a computer program. However, many people enjoy classic movies like 'The Shawshank Redemption' and 'The Godfather'."]],
    [r"how do I stay healthy", ["Staying healthy involves a balanced diet, regular exercise, adequate sleep, and managing stress. It's also important to have regular check-ups with healthcare professionals."]],
    [r"(.*)interesting fact(.*)", ["Certainly! Did you know that honeybees can recognize human faces? Researchers have found that bees can remember and recognize human faces, which is a remarkable cognitive ability for such small creatures."]],
    [r"what is the speed of light", ["The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s) or about 186,282 miles per second (mi/s)."]],
    [r"(.*)tell me a space fact(.*)", ["Certainly! Our solar system is located in the Milky Way galaxy, which is estimated to be about 13.6 billion years old."]],
    [r"what is the largest animal on Earth", ["The largest animal on Earth is the blue whale. Adult blue whales can reach lengths of up to 100 feet (30 meters) and can weigh as much as 200 tons."]],
    # Add more patterns and responses here 😊
]

chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")

    preprocessed_input = re.sub(r'[^\w\s]', '', user_input).lower()

    response = chatbot.respond(preprocessed_input)
    print("Chatbot:", response)
