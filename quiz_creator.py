#import colorama
from colorama import init, Fore, Style

#initialize colorama
init()

def format(num):
    #ask user for their question input
    question = input(Fore.YELLOW + Style.BRIGHT + f"\nEnter a question no. {num}: " + Style.RESET_ALL)

    #ask for options
    option_a = input(Fore.YELLOW + "Enter option a: " + Style.RESET_ALL)
    option_b = input(Fore.YELLOW + "Enter option b: " + Style.RESET_ALL)
    option_c = input(Fore.YELLOW + "Enter option c: " + Style.RESET_ALL)
    option_d = input(Fore.YELLOW + "Enter option d: " + Style.RESET_ALL)

    #ask for the correct answer
    correct_ans = input(Fore.GREEN + Style.BRIGHT + "\nEnter the correct answer: " + Style.RESET_ALL).lower()

    text_file = open("text_file.txt", "a")

    text_file.write("\n=============================================")
    text_file.write(f"\n{num}. {question}\n\na. {option_a}\nb. {option_b}\nc. {option_c}\nd. {option_d}\nCorrect Answer: {correct_ans}\n")
    text_file.write("=============================================\n")

    text_file.close()

    if correct_ans == "a":
        print("\na. ", Fore.GREEN + Style.BRIGHT + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL) 
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED + option_d + Style.RESET_ALL)

    elif correct_ans == "b":
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.GREEN + Style.BRIGHT + option_b + Style.RESET_ALL)
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED +  option_d + Style.RESET_ALL)

    elif correct_ans == "c":
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL)
        print("c. ", Fore.GREEN + Style.BRIGHT + option_c + Style.RESET_ALL)
        print("d. ", Fore.RED +  option_d + Style.RESET_ALL)

    else:
        print("\na. ", Fore.RED + option_a + Style.RESET_ALL)
        print("b. ", Fore.RED + option_b + Style.RESET_ALL)
        print("c. ", Fore.RED + option_c + Style.RESET_ALL)
        print("d. ", Fore.GREEN + Style.BRIGHT + option_d + Style.RESET_ALL)
           
num = 1
while True:
    format(num)
    again = input("\nAdd another question? (yes/no): ").lower()
    num += 1
    if again != "yes":
        break