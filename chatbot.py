def chatbot():
    while True:
        user = input("You : ").strip().lower()
        if user in ['hi','hello','hii']:
            print('chatbot : Hi!')
        elif user in['how are you']:
            print("chatbot : I'm fine, thanks!")
        elif user in ['bye','goodbye','byy']:
            print("chatbot : Goodbye! ")
            break
        else:
            print("I don't understand what you want to say?")

chatbot()