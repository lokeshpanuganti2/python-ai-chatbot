def chatbot():

    print("🤖 Welcome to Python Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! How are you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "calculator":
            calculator()

        elif user_input == "bye":
            print("Bot: Goodbye! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


def calculator():

    print("\n--- Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("Bot: Cannot divide by zero.")
                return
            result = num1 / num2

        else:
            print("Bot: Invalid operator.")
            return

        print("Bot: Result =", result)

    except ValueError:
        print("Bot: Please enter valid numbers.")


if __name__ == "__main__":
    chatbot()