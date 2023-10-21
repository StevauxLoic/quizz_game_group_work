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



'''
def doing_level(level, wrong_answer_max_per_question, number_of_bad_answers_in_total, number_of_good_answers_in_total, questions_amount) :
    shuffle(level)
    number_of_bad_answers_in_level = 0
    number_of_good_answers_in_level = 0                              # cahnged
    if questions_amount >= len(level):
        # the amount is greater or equal to the lenght so we keep it like it was
        adjustedLevel = level
    else:
        # we take only the needed questions
        adjustedLevel = level[:(questions_amount)]

    for question in adjustedLevel :     # we use the adjusted level                     # cahnged
        number_of_fail = 0
        question_text = question["question"]    # cahnged
        answers = question["answers"]           # cahnged
        while(number_of_fail < wrong_answer_max_per_question) :
            print(f"\nQuestion : {question_text}\n"                     # cahnged
                  f"A. {answers['A']}\n"
                  f"B. {answers['B']}\n"
                  f"C. {answers['C']}\n")
            
            answer = input("Your choice (letter) : ")                 # changed

            if(answer.upper() == question["correct_answer"]) : 
                print("Correct answer !")       # changed
                number_of_good_answers_in_level +=1
                number_of_good_answers_in_total += 1
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")
                    number_of_bad_answers_in_level += 1
                    number_of_bad_answers_in_total += 1

        if(number_of_fail == wrong_answer_max_per_question) :
            number_of_bad_answers_in_level += 1
            number_of_bad_answers_in_total += 1
            good_answer = question["answers"][question["correct_answer"]]       # cahnged
            print(f"you lost. The correct answer was {good_answer}")            # changed
            return False, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level

    return True, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level
'''

from random import shuffle

def doing_level(level, wrong_answer_max_per_question, 
                number_of_bad_answers_in_total, 
                number_of_good_answers_in_total, 
                questions_amount) :
    
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
        shuffle(answers)                                            # changed

        while(number_of_fail < wrong_answer_max_per_question) :     # changed
            print(f"\nQuestion : {question_text}")                  # changed
            for answer_index in range(len(answers)):                # changed
                print(f"{answer_index}. {answers[answer_index]}")   # changed
            
            print("Please choose a number")
            selected_answer = ask_number(1, len(answers))   # changed

            if(answers[selected_answer - 1] == question["correct_answer"]) :
                print("Correct answer !")
                number_of_good_answers_in_level +=1
                number_of_good_answers_in_total += 1
                break
            else :
                number_of_fail += 1
                if(number_of_fail < wrong_answer_max_per_question) :
                    print(f"you failed, you have {wrong_answer_max_per_question - number_of_fail} attempt left")
                    number_of_bad_answers_in_level += 1
                    number_of_bad_answers_in_total += 1

        if(number_of_fail == wrong_answer_max_per_question) :
            number_of_bad_answers_in_level += 1
            number_of_bad_answers_in_total += 1
            good_answer = question["answers"][question["correct_answer"]]
            print(f"you lost. The correct answer was {good_answer}")
            return False, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level

    return True, number_of_bad_answers_in_total, number_of_good_answers_in_total, number_of_bad_answers_in_level, number_of_good_answers_in_level