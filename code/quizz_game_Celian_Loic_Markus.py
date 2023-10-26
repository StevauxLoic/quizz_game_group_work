"""
This is a quizz game made by :
C. Célian
L. Markus
S. Loïc
"""

from random import shuffle
import os
 
class bcolors:
    """
    This class have value usable to change the colors or font's styles
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def terminal_clear():
    """
    Clears the terminal screen.

    This function checks the operating system and clears the terminal screen accordingly.
    On Unix-based systems, it uses the 'clear' command, while on Windows it uses the 'cls' command.

    Returns:
        int: 0 if the command was executed successfully, non-zero otherwise.
    """
    if os.name == 'posix':
        return os.system('clear')
    else:
        return os.system('cls')


def get_questions_lists() -> list:
    """
    Returns a list of dictionaries, where each dictionary represents a question and its possible answers.
    Each dictionary has the following keys:
    - question: a string representing the question
    - answers: a list of strings representing the possible answers
    - correct_answer: a string representing the correct answer

    Returns:
    A list of dictionaries, where each dictionary represents a question and its possible answers.
    """
    quizz = []

    level_1 = [
        {"question": "1+1 = ?",
            "answers": ["4", "-1", "2"], "correct_answer": "2"},
        {"question": "2+3 = ?",
            "answers": ["5", "10", "8"], "correct_answer": "5"},
        {"question": "5+5 = ?",
            "answers": ["12", "10", "5"], "correct_answer": "10"},
        {"question": "10+7 = ?",
            "answers": ["17", "15", "7"], "correct_answer": "17"},
        {"question": "The name of the planet you live on is?", 
            "answers": [ "Mars",  "Earth",  "TRAPPIST-1e"], "correct_answer": "Earth"},
        {"question": "In which city can you find the Eiffel Tower?",
            "answers": [ "Pori",  "Boston",  "Paris"], "correct_answer": "Paris"},
        {"question": "What do you get if you mix red and yellow?",
            "answers": [ "Lila",  "Orange",  "Green"], "correct_answer": "Orange"},
        {"question": "what's the first letter of the alphabet ?",
            "answers": [ "A",  "B",  "C"], "correct_answer": "A"},
        {"question": "what's the result of 2 + 5 ?",
            "answers": [ "6",  "7",  "9"], "correct_answer": "7"},
        {"question": "what's the longest word between those words ?",
            "answers": [ "moto",  "pineapple",  "airplane"], "correct_answer": "pineapple"},
        {"question": "what's the color of the sky ?",
            "answers": [ "brown",  "green",  "blue"], "correct_answer": "blue"},
        {"question": "what's the result of 9-2 ?",
            "answers": [ "5",  "7",  "8"], "correct_answer": "7"}
        ]
    quizz.append(level_1)

    level_2 = [
        {"question": "1*1 = ?",
            "answers": ["0", "11", "1"], "correct_answer": "1"},
        {"question": "2*3 = ?",
            "answers": ["9", "6", "5"], "correct_answer": "6"},
        {"question": "5*5 = ?",
            "answers": ["25", "20", "55"], "correct_answer": "25"},
        {"question": "10*7 = ?",
            "answers": ["70", "75", "69"], "correct_answer": "70"},
        {"question": "Which school did Harry Potter attend?",
            "answers": [ "Hogwarts",  "MIT",  "SAMK"], "correct_answer": "Hogwarts"},
        {"question": "Which is faster, light or sound?",
            "answers": [ "Sound",  "Light",  "Equally fast"], "correct_answer": "Light"},
        {"question": "In which country is the Great Wall?",
            "answers": [ "USA",  "China",  "Mongolia"], "correct_answer": "China"},
        {"question": "What's the capital of Belgium ?",
            "answers": [ "Antwerpen",  "Brussels",  "Paris"], "correct_answer": "Brussels"},
        {"question": "WHat's the biggest country ?",
            "answers": [ "Finland",  "Russia",  "USA"], "correct_answer": "Russia"},
        {"question": "What's the symbol of the oxygen in the periodic table ?",
            "answers": [ "Wu",  "Na",  "O"], "correct_answer": "O"},
        {"question": "What is the most famous series of books that J.K. Rowling wrote ?",
            "answers": [ "harry potter",  "Sherlock Homlmes",  "Lord of the rings"], "correct_answer": "harry potter"},
        {"question": "Is Hades one of Zeus's brothers in the greek mythology ?",
            "answers": [ "yes",  "no",  "Zeus does not have any brothers"], "correct_answer": "yes"}
    ]
    quizz.append(level_2)

    level_3 = [
        {"question": "(1+1) * 4 = ?",
            "answers": ["10", "8", "16"], "correct_answer": "8"},
        {"question": "(2+3) * 6 = ?",
            "answers": ["30", "36", "12"], "correct_answer": "30"},
        {"question": "(5+5) * 10 = ?",
            "answers": ["100", "250", "25"], "correct_answer": "100"},
        {"question": "(10+7) * 2 = ?",
            "answers": ["44", "24", "34"], "correct_answer": "34"},
        {"question": "What is the capital of Afghanistan?",
            "answers": [ "Miami",  "Istanbul",  "Kabul"], "correct_answer": "Kabul"},
        {"question": "Name the high IQ society founded in Oxford in 1946?",
            "answers": [ "Mensa",  "Nasa",  "Illuminati"], "correct_answer": "Mensa"},
        {"question": "Who was the Ancient Greek God of the Sun?",
            "answers": [ "Hades",  "Apollo",  "Zeus"], "correct_answer": "Apollo"},
        {"question": "What is the number 0110 1101 (base 2) in base 10 ?",
            "answers": [ "98",  "226",  "109"], "correct_answer": "109"},
        {"question": "What's the name of the band that made 'Back in black' ?",
            "answers": [ "ACDC",  "Queen",  "Gun's n Roses"], "correct_answer": "ACDC"},
        {"question": "Can a guitar have more than 6 strings ?",
            "answers": [ "yes",  "no",  "only bass can have 6 strings"], "correct_answer": "yes"},
        {"question": "What is 15°C in Fahrenheit ?",
            "answers": [ "44°F",  "37°F",  "59°F"], "correct_answer": "59°F"},
        {"question": "How many countries is there on earth (in september 2023) ?",
            "answers": [ "206", "188",  "195"], "correct_answer": "195"}
    ]
    quizz.append(level_3)

    return quizz


def doing_level(level, wrong_answer_max_per_question, 
                number_of_bad_answers_in_total, 
                number_of_good_answers_in_total, 
                questions_amount) -> tuple:
    """
    This function takes a level of questions, shuffles them, and presents them to the user. 
    For each question, the user has a limited number of attempts to answer correctly. 
    The function returns the number of bad and good answers in the level and in total.

    Args:
    - level (list): a list of dictionaries representing the questions and their answers.
    - wrong_answer_max_per_question (int): the maximum number of wrong answers allowed per question.
    - number_of_bad_answers_in_total (int): the number of bad answers in total.
    - number_of_good_answers_in_total (int): the number of good answers in total.
    - questions_amount (int): the number of questions to be presented to the user.

    Returns:
    - A tuple containing:
        - a boolean indicating whether the user succeeded in answering all the questions in the level.
        - the updated number of bad answers in total.
        - the updated number of good answers in total.
        - the number of bad answers in the current level.
        - the number of good answers in the current level.
    """
    shuffle(level)
    number_of_bad_answers_in_level = 0
    number_of_good_answers_in_level = 0

    if questions_amount >= len(level):
        # the amount is greater or equal to the lenght so we keep it like it was
        adjustedLevel = level
    else:
        # we take only the needed questions
        adjustedLevel = level[:(questions_amount)]

    for question in adjustedLevel :
        number_of_fail = 0
        question_text = question["question"]
        answers = question["answers"]
        shuffle(answers)  

        while(number_of_fail < wrong_answer_max_per_question) :
            print(f"\n{bcolors.UNDERLINE}Question : {question_text}{bcolors.ENDC}\n")
            for answer_index in range(len(answers)):
                print(f"{answer_index + 1}. {answers[answer_index]}")
            
            print("Please choose a number")
            selected_answer = ask_number(1, len(answers))

            if(answers[selected_answer - 1] == question["correct_answer"]) :
                print(f"{bcolors.OKGREEN}Correct answer !{bcolors.ENDC}")
                number_of_good_answers_in_level +=1
                number_of_good_answers_in_total += 1
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"{bcolors.WARNING}you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left{bcolors.ENDC}")
                    number_of_bad_answers_in_level += 1
                    number_of_bad_answers_in_total += 1

        if(number_of_fail == wrong_answer_max_per_question) :
            number_of_bad_answers_in_level += 1
            number_of_bad_answers_in_total += 1
            good_answer = question["correct_answer"]
            print(f"{bcolors.WARNING}you lost. The correct answer was {good_answer}{bcolors.ENDC}")
            return False, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level

    return True, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level

def ask_number(min, max) -> int:
    """
    Prompts the user to enter a number between the given minimum and maximum values (inclusive).
    If the user enters an invalid input, the function will continue to prompt the user until a valid input is entered.

    Args:
        min (int): The minimum value that the user can enter.
        max (int): The maximum value that the user can enter.

    Returns:
        int: The number entered by the user.
    """
def ask_number(min, max) -> int:
    while True:
        user_input = input(f"{bcolors.OKCYAN}Enter a number greater or equal to {min} and smaller or equal to {max} : {bcolors.ENDC}")
        if(user_input.isdigit()) :
            number_entered = int(user_input)
            if(number_entered >= min and number_entered <= max):
                return number_entered

        print(f"{bcolors.FAIL}wrong input !{bcolors.ENDC}")

def game_settings(quizz) -> tuple:
    """
    This function prompts the user to enter the game settings, including the maximum number of wrong answers per question,
    the starting level, and the maximum number of questions for each level.

    Parameters:
    quizz (list): A list of lists representing the quiz questions and answers for each level.

    Returns:
    - A tuple containing: 
        - the maximum number of wrong answers per question
        - the starting level number
        - and the maximum number of questions for each level.
    """
    print("Enter the number of max try answers per question")
    max_wrong_answers_per_question = ask_number(1, 3)

    print("Enter the number of the starting level")
    level_number = ask_number(1, len(quizz))

    print("Enter the max amount of questions for each levels")
    max_question = 0
    for level in quizz[level_number - 1:] :
        if(len(level) > max_question) :
            max_question = len(level)

    questions_amount = ask_number(1, max_question)

    return max_wrong_answers_per_question, level_number, questions_amount

def get_accuracy(good_answers_amount, bad_answers_amount) -> float:
    """
    Calculates the accuracy of the quiz game based on the number of good and bad answers.

    Args:
        good_answers_amount (int): The number of good answers.
        bad_answers_amount (int): The number of bad answers.

    Returns:
        float: The accuracy of the quiz game as a percentage.
    """
    accuracy = good_answers_amount/(good_answers_amount + bad_answers_amount)
    return accuracy

def get_answers_stat(good_answers_amount, bad_answers_amount) -> str:
    """
    Returns a string containing statistics about the number of good and bad answers given, as well as the accuracy of the answers.

    Args:
    - good_answers_amount (int): The number of good answers given.
    - bad_answers_amount (int): The number of bad answers given.

    Returns:
    - output_message (str): A string containing the following information:
        - The number of good answers given.
        - The number of bad answers given.
        - The accuracy of the answers, expressed as a percentage.
    """
    answers_accuracy = get_accuracy(good_answers_amount, bad_answers_amount)

    output_message = f"Good answers given : {good_answers_amount}\n"
    output_message += f"Bad answers given : {bad_answers_amount}\n"
    output_message += f"Answers accuracy : {answers_accuracy*100:.2f}%\n"

    return output_message

def show_game_ending(is_success, 
                     max_wrong_answers_per_question, 
                     good_answers_amount, 
                     bad_answers_amount, 
                     ending_level, 
                     starting_level=1):
    """
    Displays the statistics of the quiz game, including the number of correct and incorrect answers, 
    the starting and ending level, and whether the player succeeded or failed. Also displays a message 
    based on the player's accuracy and success status.

    Args:
    - is_success (bool): Whether the player succeeded or failed the quiz game.
    - max_wrong_answers_per_question (int): The maximum number of wrong answers allowed per question (for the last quizz try).
    - good_answers_amount (int): The number of correct answers.
    - bad_answers_amount (int): The number of incorrect answers.
    - ending_level (int): The level the player ended on (for the last quizz try).
    - starting_level (int): The level the player started on. Default is 1 (for the last quizz try).
    """
    output_message = f"{bcolors.OKBLUE}{bcolors.BOLD}########### STATS FROM THE WHOLE QUIZZES ###############{bcolors.ENDC}\n"
    output_message += get_answers_stat(good_answers_amount, bad_answers_amount)
    output_message += f"{bcolors.OKBLUE}{bcolors.BOLD}############## STATS OF THE LAST QUIZZ #################{bcolors.ENDC}\n"
    output_message += f"Starting level : {starting_level}\n"
    output_message += f"Max wrong answers per question selected : {max_wrong_answers_per_question}\n"
    output_message += f"Last level : {ending_level}\n"
    output_message += f"You {f'{bcolors.OKGREEN}succeed' if is_success else f'{bcolors.WARNING}failed'}{bcolors.ENDC}\n"

    # and using the time wait
    global_accuracy = get_accuracy(good_answers_amount, bad_answers_amount)

    if is_success:
        output_message += bcolors.OKGREEN
        if global_accuracy < 0.5:
            output_message += f"How lucky you are"
        elif global_accuracy < 0.9:
            output_message += f"Well played, good"
        else:
            output_message += f"Well done you're so precise, Amazing :)"
    else:
        output_message += bcolors.WARNING
        if global_accuracy < 0.5:
            output_message += f"You need to study a bit more..."
        elif global_accuracy < 0.9:
            output_message += f"Hoping you will do better next time"
        else:
            output_message += f"You were so close, How did you failed ? :("

    output_message += f"{bcolors.ENDC}\n"

    print(output_message)

def quizz_game() :
    """
    Runs the quiz game, which consists of several levels of questions with increasing difficulty.
    At each level, the player must answer a certain number of questions correctly without exceeding a certain number of wrong answers.
    The game ends when the player completes all levels or loses a level and chooses not to restart.
    """

    total_number_bad_answers = 0
    total_number_good_answers = 0

    quizz = get_questions_lists()
    
    terminal_clear()
    max_wrong_answers_per_question, starting_level, max_questions_amount = game_settings(quizz)
    actual_level_index = starting_level - 1

    while True:
        is_success, total_number_bad_answers, total_number_good_answers, number_of_bad_answers_in_level, number_of_good_answers_in_level = doing_level(
            quizz[actual_level_index],
            max_wrong_answers_per_question, 
            total_number_bad_answers, 
            total_number_good_answers, 
            max_questions_amount
        )

        terminal_clear()
        print(f"{bcolors.OKBLUE}{bcolors.BOLD}############## STATS FROM THE LEVEL N°{actual_level_index + 1} ################{bcolors.ENDC}")
        print(get_answers_stat(number_of_good_answers_in_level, number_of_bad_answers_in_level))

        if(is_success) :
            print(f"{bcolors.OKGREEN}you succeeded the level{bcolors.ENDC}")

            if(actual_level_index + 1 < len(quizz)) :
                actual_level_index += 1
            else :
                break
        else :
            choice_to_restart = input(f"{bcolors.FAIL}You lost !{bcolors.ENDC} Do you want to restart ?\n"
                                      f"{bcolors.OKCYAN}Type : y(yes) or anything else for no : {bcolors.ENDC}")
            terminal_clear()

            if(choice_to_restart.lower() == 'y' or choice_to_restart.lower() == 'yes'):
                max_wrong_answers_per_question, starting_level, max_questions_amount = game_settings(quizz)
                actual_level_index = starting_level - 1
            else :
                break

    
    show_game_ending(is_success, 
                     max_wrong_answers_per_question, 
                     total_number_good_answers, 
                     total_number_bad_answers, 
                     actual_level_index + 1, 
                     starting_level)


if __name__ == "__main__" :
    quizz_game()
