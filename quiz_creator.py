#ask user for their first input
question = input("Input question:\n> ")

#ask for options
option_a = input("Type choice a: ")
option_b = input("Type choice b: ")
option_c = input("Type choice c: ")
option_d = input("Type choice d: ")

#ask for the correct answer
correct_ans = input("Correct anwer is: ")

text_file = open("text_file.txt", "a")

text_file.write(f"{question}\n{option_a}\n{option_b}\n{option_c}\n{option_d}\ncorrect answer: {correct_ans}")

text_file.close()