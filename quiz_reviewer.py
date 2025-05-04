import json

def yes_no_input():
    while True:
        again = input("Do you want to add another question? (yes/no): ").lower()
        if again in ["yes", "no"]:
            return again  # Return the valid input to use outside
        else:
            print("Invalid input. Try (yes/no)")

num = 1
while True:
    #ask user for inputs like question, options, and correct answer
    questions = input(f"\nEnter question {num}: ")
    options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
    correct_answers = input(f"Enter correct answer: ")

    #dictionary for users' input
    data_format = {
        "question: ": questions,
        "option: ": options, 
        "correct answer: ": correct_answers
    }
    #initialize a list
    quiz_data = []

    #then appends the input to the list
    quiz_data.append(data_format)

    #open a json file to store the data
    with open("json_text.json", "w") as file:
        json.dump(data_format, file, indent=4)

    #asks the user to input another
    again = yes_no_input()
    num += 1
    if again != "yes":
        break