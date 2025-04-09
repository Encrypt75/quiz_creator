def format(num):
    #ask user for their first input
    question = input(f"\nInput question no. {num}: ")

    #ask for options
    option_a = input("Type choice a: ")
    option_b = input("Type choice b: ")
    option_c = input("Type choice c: ")
    option_d = input("Type choice d: ")

    #ask for the correct answer
    correct_ans = input("Correct answer is: ")

    text_file = open("text_file.txt", "a")

    text_file.write(f"{num}. {question}\na. {option_a}\nb. {option_b}\nc. {option_c}\nd. {option_d}\nCorrect Answer: {correct_ans}\n\n")

    text_file.close()

    return None

num = 1
while True:
    format(num)
    again = input("Add another question? (yes/no): ").lower()
    num += 1
    if again != "yes":
        break