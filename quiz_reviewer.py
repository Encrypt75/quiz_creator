import json
import os

#loads data from a json file
def file_load():
    if os.path.exists("json_text.json"):
        with open("json_text.json", "r") as file:
            try:
                quiz_data = json.load(file)
                if not isinstance(quiz_data, list):
                    return []
            except json.JSONDecodeError:
                    pass
    return []

#callout file_load()
quiz_data = file_load()   

#where the loop begins
while True: 
        #ask user for inputs like question, options, and correct answer
        questions = input(f"\nEnter question: ")
        options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
        correct_answers = input(f"Enter correct answer: ").lower()

        #creates dictionary for users' input
        data_format = {
            "question: ": questions,
            "option: ": options, 
            "correct answer: ": correct_answers
        }

        #then appends the input to the list
        quiz_data.append(data_format)

        try_again = input("add another question? (y/n): ").lower()

        if try_again == "n" or try_again == "no":
            break

#open a json file to store the data
with open("json_text.json", "w") as file:
    json.dump(data_format, file, indent=4)