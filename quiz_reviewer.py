import json
import os
import random
from colorama import init, Fore, Style

init()

comments = [
     "wow you are great",
     "how do you know that one?",
     "you are bright",
     "are you trying to ace it?",
     "nice!",
     "is is just me? or are you killing it"
]

rand_cmmnts = random.choice(comments)

#error handling
def valid_input(correct_letter):
    valid_input_for_choices = ["a", "b", "c", "d"]

    while True:
        select = input(correct_letter).lower()

        if select in valid_input_for_choices:
            return select
        else:
            print("Invalid input, try again")

#loads data from a json file
def file_load():
    if os.path.exists("json_text.json"):
        with open("json_text.json", "r") as file:
            try:
                quiz_data = json.load(file)
                if isinstance(quiz_data, list):
                    return quiz_data
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
        questions = input(Fore.YELLOW + Style.BRIGHT + f"\nEnter question: " + Style.RESET_ALL)
        options = [input(f"Enter option {choice}: ") for choice in ["a", "b", "c", "d"]]
        correct_answers = valid_input(f"Enter correct answer: ").lower()

        #creates dictionary for users' input
        data_format = {
            "question": questions,
            "option": options, 
            "correct_answer": correct_answers
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
    init_score = 0
    for quiz in quiz_data:
        print(Fore.BLUE + Style.BRIGHT + f"\n{quiz['question']}" + Style.RESET_ALL)
        for letter, opt in zip(["a", "b", "c", "d"], quiz["option"]):
            print(Fore.YELLOW + f"{letter}. {opt}" + Style.RESET_ALL)

        answer = valid_input("your answer: ").lower()
        if answer == quiz["correct_answer"]:
            print(Fore.GREEN + Style.BRIGHT + f"correct, {rand_cmmnts}"+ Style.RESET_ALL)
            init_score += 1

        else:
            print(Fore.RED + Style.BRIGHT + f"Incorrect. The correct answer was: {quiz['correct_answer']}" + Style.RESET_ALL)
    
    if init_score == len(quiz_data):
        print(f"PERFECT!\nscore: {init_score}/{len(quiz_data)}")

    elif init_score >= 0.75 * int(len(quiz_data)):
        print(f"CONGRATS!\nscore: {init_score}/{len(quiz_data)}")

    else:
        print(f"you did great, try again next time\nscore: {init_score}/{len(quiz_data)}")

#main program
def main_program():
     while True:
        choice = valid_input(Fore.MAGENTA + "\nProgram Menu:\na.) add questions\nb.) take a quiz\nc.) exit program\n=> " + Style.RESET_ALL).lower().strip()

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