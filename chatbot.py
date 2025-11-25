from utils import load_intents, find_response

def main():
    print("Python Chatbot is Online! (type 'exit' to quit)")
    intents = load_intents()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        response = find_response(intents, user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
