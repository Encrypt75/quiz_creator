import json

#ask user for inputs like question, options, and correct answer
questions = input("Enter question: ")
options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
correct_answers = input("Enter correct answer: ")

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