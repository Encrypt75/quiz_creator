#import colorama
from colorama import init, Fore, Style

#initialize colorama
init()

#ask user for their question input
question = input(Fore.YELLOW + Style.BRIGHT + "Enter a question: " + Style.RESET_ALL)

#asks the user for possible answers
option_a = input(Fore.YELLOW + "Enter option a: " + Style.RESET_ALL)
option_b = input(Fore.YELLOW + "Enter option b: " + Style.RESET_ALL)
option_c = input(Fore.YELLOW + "Enter option c: " + Style.RESET_ALL)
option_d = input(Fore.YELLOW + "Enter option d: " + Style.RESET_ALL)

#identify what is the correct answer
correct_answer = input(Fore.GREEN + Style.BRIGHT + "\nEnter the correct answer: " + Style.RESET_ALL).lower()

#conditional statements
if correct_answer == "a":
    print(Fore.GREEN + Style.BRIGHT + option_a + Style.RESET_ALL)
    print(Fore.RED + option_b + Style.RESET_ALL)
    print(Fore.RED + option_c + Style.RESET_ALL)
    print(Fore.RED + option_d + Style.RESET_ALL)

elif correct_answer == "b":
    print(Fore.RED + option_a + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + option_b + Style.RESET_ALL)
    print(Fore.RED + option_c + Style.RESET_ALL)
    print(Fore.RED +  option_d + Style.RESET_ALL)

elif correct_answer == "c":
    print(Fore.RED + option_a + Style.RESET_ALL)
    print(Fore.RED + option_b + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + option_c + Style.RESET_ALL)
    print(Fore.RED +  option_d + Style.RESET_ALL)

else:
    print(Fore.RED + option_a + Style.RESET_ALL)
    print(Fore.RED + option_b + Style.RESET_ALL)
    print(Fore.RED + option_c + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + option_d + Style.RESET_ALL)

#gives the user a heads up that their question was saved already
print(Fore.GREEN + "Your question is saved." +  Style.RESET_ALL)