"""
we add a max of questions per level
I say max because it could be less
example : level1(9 q) level2(12 q) level3(15 q) level(12 q)

if the user want 10 questions per level, it' not possible for the level1 but we can 
ask him 10 for each level and only 9 for the level1 (==> version 1)

Or we can check the max question we have per level but if he want to 
start form the level 2 we can just check the len() of 
all the level he will have (level2, levle3) (==> version 2)
"""


# VERSION 1

from random import shuffle

def doing_level(level, wrong_answer_max_per_question, questions_amount) : # add questions_amount
    shuffle(level)

    if questions_amount >= len(level):
        # the amount is greater or equal to the lenght so we keep it like it was
        adjustedLevel = level
    else:
        # we take only the needed questions
        adjustedLevel = level[:(questions_amount-1)]

    for question in adjustedLevel :     # we use the adjusted level
        number_of_fail = 0
        question_text = question["question"]
        answers = question["answers"]
        while(number_of_fail < wrong_answer_max_per_question) :
            print(f"\nQuestion : {question_text}\n"
                  f"A. {answers['A']}\n"
                  f"B. {answers['B']}\n"
                  f"C. {answers['C']}\n")
            
            answer = input("Your choice (letter) : ")

            if(answer.upper() == question["correct_answer"]) :
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")

        if(number_of_fail == wrong_answer_max_per_question) :
            good_answer = question["answers"][question["correct_answer"]]
            print(f"you lost. The correct answer was {good_answer}")
            return False

    return True

def quizz_game() :
    number_of_good_answers = 0
    number_of_bad_answers = 0
    
    level_1 = [...]
    level_2 = [...]
    level_3 = [...]

    quizz = [level_1, level_2, level_3]

    max_wrong_answers_per_question, starting_level = game_settings()

    # ask the number here and be sure that it's
    # less thant the lenght of the level he will attempt (min_level_lenght)
    max_question_per_level = ask/game_settings


    actual_level_index = starting_level - 1

    while True:
        is_success = doing_level(quizz[actual_level_index],max_wrong_answers_per_question)
        if(is_success) :
            print(f"you succeeded the level number {actual_level_index + 1}")

            if(actual_level_index + 1 < len(quizz)) :
                actual_level_index += 1
            else :
                break
        else :
            choice_to_restart = input("You lost ! Do you want to restart (y(yes) or anything else for no) : ")
            if(choice_to_restart.lower() == 'y' or choice_to_restart.lower() == 'yes'):
                max_wrong_answers_per_question, starting_level = game_settings()
                actual_level_index = starting_level - 1
            else :
                break


    if(is_success == False) :
        print(f"You lost at level {actual_level_index + 1}")
    else :
        print(f"well played you won all the {actual_level_index} levels")






# VERSION 2

from random import shuffle

def doing_level(level, wrong_answer_max_per_question, questions_amount) : # add questions_amount
    shuffle(level)
    for question in level[: (questions_amount-1)] :     # just use the right amount of questions (-1 becasue we start from 0 and not 1)
        number_of_fail = 0
        question_text = question["question"]
        answers = question["answers"]
        while(number_of_fail < wrong_answer_max_per_question) :
            print(f"\nQuestion : {question_text}\n"
                  f"A. {answers['A']}\n"
                  f"B. {answers['B']}\n"
                  f"C. {answers['C']}\n")
            
            answer = input("Your choice (letter) : ")

            if(answer.upper() == question["correct_answer"]) :
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")

        if(number_of_fail == wrong_answer_max_per_question) :
            good_answer = question["answers"][question["correct_answer"]]
            print(f"you lost. The correct answer was {good_answer}")
            return False

    return True

def quizz_game() :
    number_of_good_answers = 0
    number_of_bad_answers = 0
    
    level_1 = [...]
    level_2 = [...]
    level_3 = [...]

    quizz = [level_1, level_2, level_3]

    max_wrong_answers_per_question, starting_level = game_settings()


    """
    min_level_lenght = len(quizz[starting_level-1])
    for level in quizz[starting_level-1]:
        level_lenght = len(level)
        if min_level_lenght > level_lenght:
            min_level_lenght = level_lenght
    """
    # ask the number here and be sure that it's
    # less thant the lenght of the level he will attempt (min_level_lenght)
    question_amount_per_level = ask/game_settings


    actual_level_index = starting_level - 1

    while True:
        is_success = doing_level(quizz[actual_level_index],max_wrong_answers_per_question, question_amount_per_level)   # add question_amount_per_level
        if(is_success) :
            print(f"you succeeded the level number {actual_level_index + 1}")

            if(actual_level_index + 1 < len(quizz)) :
                actual_level_index += 1
            else :
                break
        else :
            choice_to_restart = input("You lost ! Do you want to restart (y(yes) or anything else for no) : ")
            if(choice_to_restart.lower() == 'y' or choice_to_restart.lower() == 'yes'):
                max_wrong_answers_per_question, starting_level = game_settings()
                actual_level_index = starting_level - 1
            else :
                break


    if(is_success == False) :
        print(f"You lost at level {actual_level_index + 1}")
    else :
        print(f"well played you won all the {actual_level_index} levels")