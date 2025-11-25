import random
import json

def load_intents():
    with open("src/intents.json", "r") as file:
        return json.load(file)

def find_response(intents, user_input):
    user_input = user_input.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "I'm not sure I understand. Can you rephrase?"
