#import random module
import random

#list where the feedbacks are stored
messages = [
    "Nice one dude", 
    "That questions slaps", 
    "You're on fire", 
    "You really good at making questions", 
    "That a difficult one", 
]

#choose any phrase from messegaes
feedback = random.choice(messages)

#print
print(feedback)