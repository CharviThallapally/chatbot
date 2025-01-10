import random

# Predefined responses for the chatbot
responses = {
    "greeting": [
        "Hello! How can I help you today?", 
        "Hi there! What can I do for you?", 
        "Hey! How can I assist you?", 
        "Greetings! How may I be of service?", 
        "Hello! It's great to see you!"
    ],
    "farewell": [
        "Goodbye! Have a great day!", 
        "See you later! Take care!", 
        "Bye! Hope to see you again!", 
        "Farewell! Stay safe!", 
        "Goodbye! Keep smiling!"
    ],
    "thanks": [
        "You're welcome!", 
        "Happy to help!", 
        "No problem!", 
        "My pleasure!", 
        "Anytime! I'm here to help."
    ],
    "default": [
        "I'm not sure I understand. Can you please clarify?", 
        "Sorry, I didn't catch that. Could you rephrase?", 
        "I'm here to help! Could you give me more details?", 
        "Hmm, that's interesting. Tell me more!", 
        "I'm still learning. Could you simplify your question?"
    ],
    "feeling": [
        "I'm just a bot, but I'm here to make your day better!", 
        "I don't have feelings, but I'm happy to chat with you!", 
        "I feel great when I can help you!", 
        "I'm always in a good mood! How about you?"
    ],
    "joke": [
        "Why did the computer catch a cold? Because it left its Windows open!", 
        "Why was the robot tired? It had too many bytes!", 
        "Why don't programmers like nature? It has too many bugs!", 
        "Why was the math book sad? Because it had too many problems!"
    ]
}

# Function to categorize user input based on keywords
def get_response_category(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "greeting"
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "farewell"
    elif any(word in user_input for word in ["thanks", "thank"]):
        return "thanks"
    elif any(word in user_input for word in ["feel", "feeling"]):
        return "feeling"
    elif any(word in user_input for word in ["joke", "funny"]):
        return "joke"
    else:
        return "default"

# Function to handle user input and generate a response
def chatbot_response(user_input):
    category = get_response_category(user_input)
    if category in responses:
        return random.choice(responses[category])
    else:
        return random.choice(responses["default"])

# Main loop for user interaction
def main():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
