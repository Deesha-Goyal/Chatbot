import nltk  #nltk, a Python library for text processing
from nltk.chat.util import Chat, reflections

# Defining chatbot responses
pairs = [
    # Greetings
    ["hi|hello|hey|namaste", ["Hello! How can I assist you today? 😊", "Hey there! What's up?", "Hi! Hope you're doing well!", "Namaste 🙏"]],

    ["how are you?", ["I'm doing great! Thanks for asking. How about you?", "I'm just a bot, but I'm feeling awesome!"]],
    
    # Basic Info
    ["what is your name?|who are you?", ["I am an AI ChatBot! You can call me ChatterGoyal 🤖.", "I am ChatBot, your virtual assistant!"]],

    ["who created you?", ["I was created by an amazing coder... maybe that’s you? 😜", "A brilliant mind created me!"]],

    ["how old are you?|what's your age?", ["I don't have an age since I'm an AI but good question."]],

    ["what's your personal life?|tell me about your life", ["I don't have a personal life like humans do, since I'm an AI! 😒"]],
    
    # Jokes
    ["tell me a joke|funny jokes", ["Why did the computer catch a cold? It left its Windows open!🤣", 
                        "Parallel lines have so much in common, It's a shame they will never meet! 🤣",
                        "Why did the bicycle fall over? Because it was two-tired! 🤣",
                        "Why don't some couples go to the gym? Because some relationships don't work out! 🤣",
                        "Why don’t scientists trust atoms? Because they make up everything! 🤣"]],
    
    # Motivation
    ["motivate me|give me motivation|inspire me", 
        ["“The only way to do great work is to love what you do.” – Steve Jobs 👍", 
         "“Success is not final, failure is not fatal: It is the courage to continue that counts.” – Winston Churchill 👍",
         "“Life is what happens when you're busy making other plans.” – John Lennon 👍"]],
    
    # Fun Facts
    ["tell me a fun fact|some fun facts", 
        ["Did you know that honey never spoils? Archaeologists found 3000-year-old honey that’s still good to eat! 🍯",
         "Bananas are berries, but strawberries are not! 🍌🍓",
         "Octopuses have three hearts and blue blood! 🐙"]],
    
    # Tech Questions
    ["what is python?", ["Python is a popular programming language known for its simplicity and versatility. 🐍"]],

    ["who is the founder of google?", ["Google was founded by Larry Page and Sergey Brin in 1998."]],

    ["what is the main function of the CPU in the computer?", ["CPU stands for Central Processing Unit, it processes instructions and controls the operations of the computer."]],

    ["what is the full form of Wi-Fi?|wifi full form.", ["Wireless Fidelity"]],

    ["what is a database?", ["Database is an organized collection of data, usually stored and accessed electronically from a computer system."]],
    
    # Science and Space
    ["who discovered gravity?", ["Gravity was discovered by Sir Isaac Newton when he saw an apple fall from a tree. 🍏"]],

    ["what is the speed of light?", ["The speed of light is approximately 299,792,458 meters per second. 🚀"]],

    ["what planet is known as the Red Planet?", ["Mars."]],

    ["what gas do plants take in during photosynthesis?", ["Carbon Dioxide."]],

    ["what is the name of the galaxy we live in?", ["Milky Way Galaxy."]],
    
    # Time-related
    ["what day is it today?", ["Today is a great day to be productive! 😊", "It’s a good day to achieve something amazing!"]],
    
    # Food and Drinks
    ["what is your favorite food?", ["I love bytes and bits! But if I had to choose, I’d go for digital cookies. 🍪"]],

    ["do you drink water?", ["I stay hydrated with data streams! 💧"]],
    
    # Personal Questions (Funny Responses)
    ["are you a robot?", ["Yes, but I have feelings too... just kidding! 🤖"]],

    ["do you have emotions?", ["I try to be funny, does that count as an emotion? 😜"]],
    
    # Ending the Chat
    ["bye|goodbye|exit", ["Goodbye! Have a great day! 👋", "See you later! Keep smiling! 😊", "Bye-bye! Hope to chat again soon!"]],
]

# Creating a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start chat
def chat():
    print("\nChatterGoyal 🤖: Hello! I am your friendly ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "exit", "quit", "goodbye"]:
            print("ChatterGoyal 🤖:", "Goodbye! Have a great day! 👋")
            break

        response = chatbot.respond(user_input)
        print("ChatterGoyal 🤖:", response if response else "I'm not sure about that. Can you ask something else? 🤔")

# Run the chatbot
chat()