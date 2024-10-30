import random
import password_choices

9
def not_an_option():
    print("That is not a valid option. Try again!")
    ask_difficulty()


def ask_difficulty():
    global choices
    complexity = input("Enter password complexity (easy, medium, hard, impossible):\n")
    if complexity.lower() == "easy":
        choices = ["Letter"]
    elif complexity.lower() == "medium":
        choices = ["Letter", "Number"]
    elif complexity.lower() == "hard":
        choices = ["Letter", "Number", "Symbol"]
    elif complexity.lower() == "impossible":
        choices = ["Letter", "Number", "Symbol", "Impossible"]
    else:
        not_an_option()


length_of_password = int(input("Enter length of password:\n"))
choices = []
index = 0
password = ""
ask_difficulty()

while index != length_of_password:
    choice = random.choice(choices)
    if choice == "Letter":
        if random.choice(["Capital", "Small"]) == "Capital":
            password += random.choice(password_choices.capital_letters)
        elif random.choice(["Capital", "Small"]) == "Small":
            password += random.choice(password_choices.small_letters)
    elif choice == "Number":
        password += random.choice(password_choices.numbers)
    elif choice == "Symbol":
        password += random.choice(password_choices.symbols)
    elif choice == "Impossible":
        password += random.choice(password_choices.impossible)
    index += 1

print(f"Your password could be {password}")
