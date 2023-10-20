"""
We can create an ending function that will display all the informations
to the user as how many bad and rights choices, accuracy, ...
"""

def show_game_ending(is_success, max_wrong_answers_per_question, good_answers_amount, bad_answers_amount, ending_level, starting_level=1):
    answers_accuracy = good_answers_amount/(good_answers_amount + bad_answers_amount)

    output_message = f"########### STATS FROM THE WHOLE QUIZZ ###############\n"
    output_message += f"Max wrong answers per question : {max_wrong_answers_per_question}"
    output_message += f"Good answers given : {good_answers_amount}"
    output_message += f"Bad answers given : {bad_answers_amount}"
    output_message += f"Answers accuracy : {answers_accuracy*100}%"
    output_message += f"############# STATS OF THE LAST TRY #################\n"
    output_message += f"Starting level : {starting_level}"
    output_message += f"Last level : {ending_level}"
    output_message += f"You {'succeed' if is_success else 'failed'}"
    # here we can add some message related to the accuracy and the success
    # e.g. : success + 100% accuracy ==> 'Well done you're so precise, Amazing'
    #        failed + 90% accuracy ==> 'How did you lose ?'
    #        failed + 50% accuracy ==> 'Not so lucky'
    #        success + 50% accuracy ==> 'How lucky you are'

    # we can even add effect as colours, clear the terminal before showing anything
    # and using the time wait

    print(output_message)


def quizz_game() :
    number_of_good_answers = 0
    number_of_bad_answers = 0
    
    level_1 = [...]
    level_2 = [...]
    level_3 = [...]
    quizz = [level_1, level_2, level_3]

    max_wrong_answers_per_question, starting_level = game_settings()
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
    
    show_game_ending(is_success,                        # add this function instead of anything else
                     max_wrong_answers_per_question, 
                     number_of_good_answers, 
                     number_of_bad_answers, 
                     actual_level_index + 1, 
                     starting_level)