'''
ACTUAL CODE :

def game_settings():
    while True:
        user_input = input("Enter the number of max try answers per question ( Please select a number greater than 0): ")
        if(user_input.isdigit()) :
            if(int(user_input) > 0):
                max_wrong_answers_per_question = int(user_input)
                break
        print("wrong input ! Please select a number greater or equal than 0")

    while True:
        user_input = input("Enter the number of the starting quizz ( Please select a number between 1 - 3): ")
        if(user_input.isdigit()) :
            if(int(user_input) > 0 and int(user_input) <=3 ):
                level_number = int(user_input)
                break
    return max_wrong_answers_per_question, level_number
'''

# 1st version
def ask_number(min, max)->int:
    is_input_valid = False
    user_input = input(f"Enter a number greater or equal to {min} and smaller or equal to {max} : ")
    while not is_input_valid:
        if(user_input.isdigit()) :
            number_entered = int(user_input)
            if(number_entered >= min and number_entered <= max):
                is_input_valid = True

        print("wrong input !")
    
    return number_entered

# 2nd version
def ask_number(min, max)->int:
    user_input = input(f"Enter a number greater or equal to {min} and smaller or equal to {max} : ")
    while True:
        if(user_input.isdigit()) :
            number_entered = int(user_input)
            if(number_entered >= min and number_entered <= max):
                return number_entered

        print("wrong input !")


# game_settings cahnges
def game_settings():
    print("Enter the number of max try answers per question")
    max_wrong_answers_per_question = ask_number(1, 2)

    print("Enter the number of the starting quizz")
    level_number = ask_number(1, 3)

    return max_wrong_answers_per_question, level_number

"""
more readble
we don't repeat the code
we can even use this function if we replace 'a', 'b' and 'c' by 1, 2 and 3
we can choose between the two versions
"""