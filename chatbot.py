"""CodeAlpha Task 4: Basic Rule-Based Chatbot"""


def get_response(message):
    message = message.lower().strip()

    if "hello" in message or message in ("hi", "hey"):
        return "Hi!"
    elif "how are you" in message:
        return "I'm fine, thanks!"
    elif "your name" in message:
        return "I'm a simple Python chatbot."
    elif "help" in message:
        return "Try saying: hello, how are you, or bye."
    elif "bye" in message:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


def main():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"Chatbot: {reply}")
        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
