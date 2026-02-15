def chatbot():
    print("🤖 Simple Chatbot")
    print("Type 'exit' to stop the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "Hi":
            print("Bot: Hi!")

        elif user_input == "How are you":
            print("Bot: I am fine. Thank you!")

        elif user_input == "What is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user_input == "By":
            print("Bot: Goodbye! Have a nice day.")
            break

        elif user_input == "Exit":
            print("Bot: Chat ended.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Call the function
chatbot()
