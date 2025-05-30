#import needed modules
import random
from colorama import init, Fore, Style

#initialize colorama
init()

def valid_input(correct_letter):
    valid_input_for_choices = ["a", "b", "c", "d"]

    while True:
        select = input(correct_letter).lower()

        if select in valid_input_for_choices:
            return select
        else:
            print("Invalid input, try again")

def yes_no_input():
    while True:
        again = input("Do you want to add another question? (yes/no): ").lower()
        if again in ["yes", "no"]:
            return again  # Return the valid input to use outside
        else:
            print("Invalid input. Try (yes/no)")

#list of messages
messages = [
    "Nice question you have there", 
    "That questions slaps!", 
    "That questions on fire!", 
    "You really good at making quiz", 
    "Whoo..thats a difficult one", 
    "Even Einstien can't handle that one"
]

rand_mssg = random.choice(messages)

def format(num):
    #ask user for their question input
    question = input(Fore.YELLOW + Style.BRIGHT + f"\nEnter a question no. {num}: " + Style.RESET_ALL)

    #ask for options
    option_a = input(Fore.YELLOW + "Enter option a: " + Style.RESET_ALL)
    option_b = input(Fore.YELLOW + "Enter option b: " + Style.RESET_ALL)
    option_c = input(Fore.YELLOW + "Enter option c: " + Style.RESET_ALL)
    option_d = input(Fore.YELLOW + "Enter option d: " + Style.RESET_ALL)

    #ask for the correct answer
    correct_ans = valid_input(Fore.GREEN + Style.BRIGHT + "\nEnter the correct answer: " + Style.RESET_ALL)

    text_file = open("text_file.txt", "a")

    #format in txt file
    text_file.write(f"\n{num}. {question}\n\na. {option_a}\nb. {option_b}\nc. {option_c}\nd. {option_d}\nCorrect Answer: {correct_ans}\n")
    text_file.write("=============================================\n")

    text_file.close()

    #conditional statements
    if correct_ans == "a":
        print("\na. ", Fore.GREEN + Style.BRIGHT + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL) 
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED + option_d + Style.RESET_ALL)
        print(f"\n{rand_mssg}")

    elif correct_ans == "b":
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.GREEN + Style.BRIGHT + option_b + Style.RESET_ALL)
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED +  option_d + Style.RESET_ALL)
        print(f"\n{rand_mssg}")

    elif correct_ans == "c":
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL)
        print("c. ", Fore.GREEN + Style.BRIGHT + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED +  option_d + Style.RESET_ALL)
        print(f"\n{rand_mssg}")

    else:
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL)
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.GREEN + Style.BRIGHT + option_d + Style.RESET_ALL)
        print(f"\n{rand_mssg}")

#loop that asks the user for infinite number of times    
num = 1
while True:
    format(num)
    again = yes_no_input()  # Get the result from the function
    num += 1
    if again != "yes":
        break