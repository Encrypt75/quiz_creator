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
#checking if the dictionary works
for key in data_format:
    print(key, data_format[key])