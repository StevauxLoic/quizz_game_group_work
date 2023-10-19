from random import shuffle

def doing_level(level, wrong_answer_max_per_question) :
    shuffle(level)                              # cahnged
    for question in level :                     # cahnged
        number_of_fail = 0
        question_text = question["question"]    # cahnged
        answers = question["answers"]           # cahnged
        while(number_of_fail < wrong_answer_max_per_question) :
            print(f"\nQuestion : {question_text}\n"                     # cahnged
                  f"A. {answers['A']}\n"
                  f"B. {answers['B']}\n"
                  f"C. {answers['C']}\n")
            
            answer = input("Your choice (letter) : ")                 # changed

            if(answer.upper() == question["correct_answer"]) :        # changed
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")

        if(number_of_fail == wrong_answer_max_per_question) :
            good_answer = question["answers"][question["correct_answer"]]       # cahnged
            print(f"you lost. The correct answer was {good_answer}")            # changed
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
    
    level_1 = [
        {"question": "1+1 = ?",
         "answers": {"A":"4", "B":"-1", "C":"2"}, "correct_answer": "C"},
        {"question": "2+3 = ?",
         "answers": {"A":"5", "B":"10", "C":"8"}, "correct_answer": "A"},
        {"question": "5+5 = ?",
         "answers": {"A":"12", "B":"10", "C":"5"}, "correct_answer": "B"},
        {"question": "10+7 = ?",
         "answers": {"A":"17", "B":"15", "C":"7"}, "correct_answer": "A"},
        {"question": "The name of the planet you live on is?", 
         "answers": {"A": "Mars", "B": "Earth", "C": "TRAPPIST-1e"},"correct_answer": "B"},
        {"question": "In which city can you find the Eiffel Tower?",
         "answers": {"A": "Pori", "B": "Boston", "C": "Paris"}, "correct_answer": "C"},
        {"question": "What do you get if you mix red and yellow?",
         "answers": {"A": "Lila", "B": "Orange", "C": "Green"}, "correct_answer": "B"},
        {"question": "what's the first letter of the alphabet ?",
         "answers": {"A": "A", "B": " B", "C": "C"}, "correct_answer": "A"},
        {"question": "what's the result of 2 + 5 ?",
         "answers": {"A": "6", "B": "7", "C": "9"}, "correct_answer": "B"},
        {"question": "what's the longest word between those words ?",
         "answers": {"A": "moto", "B": "pineapple", "C": "airplane"}, "correct_answer": "B"},
        {"question": "what's the color of the sky ?",
         "answers": {"A": "brown", "B": "green", "C": "blue"}, "correct_answer": "C"},
        {"question": "what's the result of 9-2 ?",
         "answers": {"A": "5", "B": "7", "C": "8"}, "correct_answer": "B"}
    ]

    level_2 = [
        {"question": "1*1 = ?",
         "answers": {"A":"0", "B":"11", "C":"1"}, "correct_answer": "C"},
        {"question": "2*3 = ?",
         "answers": {"A":"9", "B":"6", "C":"5"}, "correct_answer": "B"},
        {"question": "5*5 = ?",
         "answers": {"A":"25", "B":"20", "C":"55"}, "correct_answer": "A"},
        {"question": "10*7 = ?",
         "answers": {"A":"70", "B":"75", "C":"69"}, "correct_answer": "A"},
        {"question": "Which school did Harry Potter attend?",
         "answers": {"A": "Hogwarts", "B": "MIT", "C": "SAMK"}, "correct_answer": "A"},
        {"question": "Which is faster, light or sound?",
         "answers": {"A": "Sound", "B": "Light", "C": "Equally fast"}, "correct_answer": "B"},
        {"question": "In which country is the Great Wall?",
         "answers": {"A": "USA", "B": "China", "C": "Mongolia"}, "correct_answer": "B"},
        {"question": "What's the capital of Belgium ?",
         "answers": {"A": "Antwerpen", "B": "Brussels", "C": "Paris"}, "correct_answer": "B"},
        {"question": "WHat's the biggest country ?",
         "answers": {"A": "Finland", "B": "Russia", "C": "USA"}, "correct_answer": "B"},
        {"question": "What's the symbol of the oxygen in the periodic table ?",
         "answers": {"A": "Wu", "B": "Na", "C": "O"}, "correct_answer": "C"},
        {"question": "What is the most famous series of books that J.K. Rowling wrote ?",
         "answers": {"A": "harry potter", "B": "Sherlock Homlmes", "C": "Lord of the rings"}, "correct_answer": "A"},
        {"question": "Is Hades one of Zeus's brothers in the greek mythology ?",
         "answers": {"A": "yes", "B": "no", "C": "Zeus does not have any brothers"}, "correct_answer": "A"}
    ]

    level_3 = [
        {"question": "(1+1) * 4 = ?",
         "answers": {"A":"10", "B":"8", "C":"16"}, "correct_answer": "B"},
        {"question": "(2+3) * 6 = ?",
         "answers": {"A":"30", "B":"36", "C":"12"}, "correct_answer": "A"},
        {"question": "(5+5) * 10 = ?",
         "answers": {"A":"100", "B":"250", "C":"25"}, "correct_answer": "A"},
        {"question": "(10+7) * 2 = ?",
         "answers": {"A":"44", "B":"24", "C":"34"}, "correct_answer": "C"},
        {"question": "What is the capital of Afghanistan?",
         "answers": {"A": "Miami", "B": "Istanbul", "C": "Kabul"},"correct_answer": "C"},
        {"question": "Name the high IQ society founded in Oxford in 1946?",
         "answers": {"A": "Mensa", "B": "Nasa", "C": "Illuminati"}, "correct_answer": "A"},
        {"question": "Who was the Ancient Greek God of the Sun?",
         "answers": {"A": "Hades", "B": "Apollo", "C": "Zeus"},"correct_answer": "B"},
        {"question": "What is the number 0110 1101 (base 2) in base 10 ?",
         "answers": {"A": "98", "B": "226", "C": "109"}, "correct_answer": "C"},
        {"question": "What's the name of the band that made 'Back in black' ?",
         "answers": {"A": "ACDC", "B": "Queen", "C": "Gun's n Roses"}, "correct_answer": "A"},
        {"question": "Can a guitar have more than 6 strings ?",
         "answers": {"A": "yes", "B": "no", "C": "only bass can have 6 strings"}, "correct_answer": "A"},
        {"question": "What is 15°C in Fahrenheit ?",
         "answers": {"A": "44°F", "B": "37°F", "C": "59°F"}, "correct_answer": "C"},
        {"question": "How many countries is there on earth (in september 2023) ?",
         "answers": {"A": "206", "B": "188", "C": "195"}, "correct_answer": "C"}
    ]
            # levels changed

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
            choice_to_restart = input("You lost ! Do you want to restart (y(yes) or anything else for no) : ")  # changes
            if(choice_to_restart.lower() == 'y' or choice_to_restart.lower() == 'yes'):
                max_wrong_answers_per_question, starting_level = game_settings()
                actual_level_index = starting_level - 1
            else :
                break


    if(is_success == False) :
        print(f"You lost at level {actual_level_index + 1}")
    else :
        print(f"well played you won all the {actual_level_index} levels")       # maybe change ==> if he start at level 2 and only fail the message will be : "well played you won all the 1 levels"



if __name__ == "__main__" :
    quizz_game()
