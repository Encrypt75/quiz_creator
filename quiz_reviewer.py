import json
import os
import random

comments = [
     "Wow you are great",
     "How do you know that one?",
     "You are bright",
     "Are you trying to ace it?",
     "Nice!",
     "Is is just me? but you are killing it"
]

rand_cmmnts = random.choice(comments)

#loads data from a json file
def file_load():
    if os.path.exists("json_text.json"):
        with open("json_text.json", "r") as file:
            try:
                quiz_data = json.load(file)
                if isinstance(quiz_data, list):
                    return []
            except json.JSONDecodeError:
                    pass
    return [] 
def data_saver(data_format):
    #open a json file to store the data
    with open("json_text.json", "w") as file:
        json.dump(data_format, file, indent=4)

def add_questions():
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
    
    data_saver(quiz_data)

def main_quiz():
    quiz_data = file_load()
    if not quiz_data:
        print("No questions was saved yet")
        return
    
    #shuffles the data from json
    random.shuffle(quiz_data)

    for quiz in quiz_data:
        print(f"\n{quiz['question']}")
        for letter, options in zip(["a", "b", "c", "d"], quiz["option"]):
            print(f"{letter}. {options}")
        answer = input("your answer: ").lower()
        if answer == quiz["correct_answer"]:
            print(rand_cmmnts)

        else:
            print(f"Incorrect. The correct answer was: {quiz['correct_answer']}")

#main program
def main_program():
     while True:
        choice = input("\nProgram Menu:\na.) add questions\nb.) take a quiz\nc.) exit program\n=>").lower().strip()

        if choice == "a":
            add_questions()
        elif choice == "b":
            main_quiz()
        elif choice == "c":
            print("exiting...")
            break
        else:
            print("invalid, try again")

#callout the main funtion 
main_program()