def chatbot():
    print("🤖 Simple Chatbot")
    print("Type 'exit' to stop the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hi":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I am fine. Thank you!")

        elif user_input == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        elif user_input == "exit":
            print("Bot: Chat ended.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Call the function
chatbot()
