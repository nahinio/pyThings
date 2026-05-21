import os

# place history file in the same folder as this script
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "history.txt")

def show_history(history):
    if not os.path.exists(history):
        print("No history found.\n")
        return

    with open(history, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found.\n")
        else:
            for line in reversed(lines):
                print(line.strip())

    print()


def clear_history():
    file = open(HISTORY_FILE, "w")
    file.write("")
    file.close()
    print("History cleared.\n")


def save_history(equation, result):
    file = open(HISTORY_FILE, "a")
    file.write(equation + " = " + str(result) + "\n")
    file.close()


def calculate(userInput):
    parts = userInput.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number\n")
        return None
    num1, operator, num2 = parts

    if operator == "+":
        result = float(num1) + float(num2)
    elif operator == "-":
        result = float(num1) - float(num2)
    elif operator == "*":
        result = float(num1) * float(num2)
    elif operator == "/":
        if float(num2) == 0:
            print("Error: Division by zero.\n")
            return None
        result = float(num1) / float(num2)
    elif operator == "^":
        result = float(num1) ** float(num2)
    elif operator == "%":
        result = float(num1) % float(num2)
    else:
        print("Invalid operator. Supported operators are: +, -, *, /, ^, %\n")
        return None

    if(int(result) == result):
        result = int(result)
    print(f'Result: {result}\n')
    save_history(userInput, result)


def main():
    print("---------------------------------------------------------")
    print()
    print("Hello! Welcome to the Calculator! (We save history btw..)\n")
    print("---------------------------------------------------------")



    while True:

        print("Available Operators: +, -, *, /, ^, %")
        print("Input format: number operator number (e.g., 2 + 3)")

        print("\nAvailable Commands:")
        print("1. history - Show calculation history")
        print("2. clear - Clear calculation history")
        print("3. exit - Exit the calculator")
        print("---------------------------------------------------------")


        userInput = input("Enter an equation or Command: ")
        
        if userInput.lower() == "exit":
            break
        elif userInput.lower() == "history":
            show_history(HISTORY_FILE)
        elif userInput.lower() == "clear":
            clear_history()
        else:
            calculate(userInput)

main()