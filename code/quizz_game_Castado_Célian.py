def doing_level(level, wrong_answer_max_per_question) :
    for question, correct_answer in level.items() :
        number_of_fail = 0
        while(number_of_fail < wrong_answer_max_per_question) :
            answer = input(question)

            if(answer == correct_answer) :
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")

        if(number_of_fail == wrong_answer_max_per_question) :
            print(f"you lost. The correct answer was {correct_answer}")
            return False

    return True


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

def quizz_game() :
    number_of_good_answers = 0
    number_of_bad_answers = 0
    level_1 = {
        "1+1 = ?" : "2",
        "2+3 = ?" : "5",
        "5+5 = ?" : "10",
        "10+7 = ?" : "17"
    }
    level_2 = {
        "1*1 = ?": "1",
        "2*3 = ?": "6",
        "5*5 = ?": "25",
        "10*7 = ?": "70"
    }
    level_3 = {
        "(1+1) * 4 = ?": "8",
        "(2+3) * 6 = ?": "30",
        "(5+5) * 10 = ?": "100",
        "(10+7) * 2 = ?": "34"
    }

    quizz = [level_1, level_2, level_3]

    max_wrong_answers_per_question, starting_level = game_settings()
    actual_level_index = starting_level - 1

    while True:
        is_success = doing_level(quizz[actual_level_index],max_wrong_answers_per_question)
        if(is_success) :
            print(f"you succed the level number {actual_level_index + 1}")

            if(actual_level_index + 1 < len(quizz)) :
                actual_level_index += 1
            else :
                break
        else :
            choice_to_restart = input("You lost ! Do you want to restart press y(yes) and press enter to not restart")
            if(choice_to_restart.lower() == 'y' or choice_to_restart.lower() == 'yes'):
                max_wrong_answers_per_question, starting_level = game_settings()
                actual_level_index = starting_level - 1
            else :
                break


    if(is_success == False) :
        print(f"You lost at level {actual_level_index + 1}")
    else :
        print(f"well played you won all the {actual_level_index} levels")



if __name__ == "__main__" :
    quizz_game()
