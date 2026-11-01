def chatbot():
    print("chatbot:, How can i help you")

    while True:
        user= input("You: " )
        user=user.lower()

        if "hii" in user:
            print("Chatbot: Hello , how are you")

        elif "college" in user:
            print("Chatbot: Nmiet pune")

        elif "course" in user:
            print("Chatbot: computer engineering")
        elif "bye"in user:
            print("Chatbot: Goodbye , Have a nice day")
            break
        else:
            print("Chatbot: Errorrr....")

chatbot()

    