# Task 1 - Rule-Based Chatbot
print("Welcome to the CodSoft Chatbot!")
while True:
    user_input = input("You: ").lower()
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("Bot: I'm an AI bot, always running! What about you?")
    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: I'm not sure how to respond to that.")
