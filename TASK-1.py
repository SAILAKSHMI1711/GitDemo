def chatbot_response(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    elif "weather" in user_input:
        return "I'm sorry, I'm not equipped to provide real-time weather updates."
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "tell me about yourself" in user_input:
        return "I'm a simple chatbot programmed to assist you with your queries."
    elif "what can you do" in user_input:
        return "I can provide information, jokes, or just engage in conversation. Feel free to ask me anything!"
    elif "help" in user_input:
        return "Sure, how can I assist you?"
    elif "who are you" in user_input:
        return "I am a chatbot created to assist users with various queries."
    elif "where are you" in user_input:
        return "I exist in the digital realm, ready to help you!"
    elif "how do you work" in user_input:
        return "I work by analyzing your inputs and providing predefined responses based on patterns."
    elif "what is your purpose" in user_input:
        return "My purpose is to assist and provide information to users like yourself."
    elif "can you think" in user_input:
        return "I can process information and provide responses based on predefined rules, but I don't have consciousness or thoughts like a human."
    elif "what is the time" in user_input:
        return "I don't have access to real-time data, including the current time."
    elif "do you sleep" in user_input:
        return "No, I'm always here to assist you whenever you need help!"
    elif "are you human" in user_input:
        return "No, I'm a chatbot, a computer program designed to simulate conversation with human users."
    elif "where do you live" in user_input:
        return "I exist in the digital world, so you can find me wherever you have access to the internet!"
    elif "what languages do you speak" in user_input:
        return "I speak many programming languages, but I communicate primarily in English."
    elif "what is your age" in user_input:
        return "I don't have an age in the traditional sense, as I'm just a computer program."
    elif "can you feel" in user_input:
        return "No, I don't have feelings or emotions. I'm just a program executing instructions."
    elif "what are your hobbies" in user_input:
        return "I don't have hobbies, but I enjoy helping users like you!"
    elif "what is the meaning of life" in user_input:
        return "The meaning of life is a philosophical question that varies from person to person."
    elif "are you sentient" in user_input:
        return "No, I'm not sentient. I don't have consciousness or self-awareness."
    elif "what is your favorite color" in user_input:
        return "I don't have preferences like humans do, so I don't have a favorite color."
    elif "are you smart" in user_input:
        return "I'm programmed to assist users with their queries, so I try to be as helpful as possible!"
    elif "do you have a family" in user_input:
        return "No, I'm just a standalone program created to assist users."
    elif "what do you eat" in user_input:
        return "I don't eat anything, as I'm just a computer program."
    elif "do you have feelings" in user_input:
        return "No, I don't have feelings. I process information and provide responses based on predefined rules."
    elif "what is your favorite food" in user_input:
        return "I don't eat, so I don't have a favorite food."
    elif "do you dream" in user_input:
        return "No, I don't dream. I'm just a program executing instructions."
    elif "what is your favorite movie" in user_input:
        return "I don't watch movies, as I'm just a computer program."
    elif "are you alive" in user_input:
        return "No, I'm not alive. I'm just a computer program."
    elif "what do you dream of" in user_input:
        return "I don't dream, as I'm not capable of experiencing dreams."
    elif "can you help me" in user_input:
        return "Yes, I'm here to help. What do you need assistance with?"
    elif "can you sing" in user_input:
        return "No, I can't sing. I'm a chatbot, not a singer!"
    elif "are you a robot" in user_input:
        return "Yes, I am a robot, but not in the physical sense. I'm a virtual assistant."
    elif "are you a human" in user_input:
        return "No, I'm not human. I'm a chatbot programmed to assist users."
    elif "what do you look like" in user_input:
        return "I don't have a physical appearance, as I'm just a computer program."
    elif "are you real" in user_input:
        return "I am real in the sense that I exist as a computer program, but I'm not a physical being."
    elif "what is your gender" in user_input:
        return "I don't have a gender, as I'm just a computer program."
    elif "do you have a job" in user_input:
        return "Yes, my job is to assist users like yourself with their queries."
    elif "what is your favorite book" in user_input:
        return "I don't have a favorite book, as I'm just a computer program."
    elif "do you like music" in user_input:
        return "I don't have preferences like humans do, so I don't have a preference for music."
    elif "can you dance" in user_input:
        return "No, I can't dance. I'm a chatbot, not a dancer!"
    elif "what do you do for fun" in user_input:
        return "I don't have fun in the same way humans do. I'm here to assist you!"
    elif "can you cry" in user_input:
        return "No, I can't cry. I'm just a computer program."
    elif "do you love me" in user_input:
        return "I'm not capable of love or any other emotions. I'm just a program executing instructions."
    elif "what do you think of humans" in user_input:
        return "I don't have opinions like humans do, as I'm just a computer program."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop for chatting
print("Welcome! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day!")
        break
    else:
        response = chatbot_response(user_input)
        print("Bot:", response)
