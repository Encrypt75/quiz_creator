#import colorama
from colorama import init, Fore, Style

#initialize colorama
init()

question = input(Fore.YELLOW + Style.BRIGHT + "Enter a question: " + Style.RESET_ALL)

print(Fore.GREEN + "Your question is saved." +  Style.RESET_ALL)