#ask user for inputs like question, options, and correct answer
question = input("Enter question: ")
options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
correct_answer = input("Enter correct answer: ")