# Assignment ------------------------------------------------------------------------------------
# 1. Run this file and take the questionnaire.
# 2. Add your questionnaire_responses.txt file to the Google Assignment submission.
# 3. Modify this file to ask Ms. Ifft at least three questions you would like to know about her.
# 4. Add your modified version of this file to your Google Assignment submission.
# ------------------------------------------------------------------------------------------------

"""
This module asks the user a series of questions.
When the user answers, the questions and answers are written to a file called questionnaire_responses.txt
"""

print("\nWelcome to the Get to Know You Questionaire!\n")

# open the file questionnaire_responses.txt in the same directory as this code, and add their name to it
questionnaire_file = open('questionnaire_responses.txt', 'w')
name = input("First, your name please: ")
questionnaire_file.write(name + "\n\n")

# create and ask some questions; then print questions and answers to a file.
questionnaire_simple_questions = [
    "And what pronouns do you use?",
    "And can you help me to understand why you took this class?",
    "What ways do you learn best?\nFor example, with a quiet environment, hands-on, listening, reading, seeing, etc.",
    "I'm so glad you're here! What are you hoping to get out of this class?",
    "In your opinion, what qualities does a great teacher have?",
    "Can you tell me about the piece of code you’ve written that you are most proud of?"
]

for question in questionnaire_simple_questions:
    print("\n" + question)
    answer = input("You can type your answer here: ")
    questionnaire_file.write(question + "\n\n")
    questionnaire_file.write(answer + "\n\n\n")

# ask last question
last_question = "Last question! Are you an introvert, or extrovert? Or an ambivert maybe? Something else?"
last_question_dict = {
    "a": "introvert",
    "b": "extrovert",
    "c": "ambivert",
    "d": "other"
}
print("\n" + last_question)
for key, value in last_question_dict.items():
    print(key.upper() + ". " + value)
introvert_extrovert_letter = input("Please enter the corresponding letter: ")
introvert_extrovert_explanation = None

while introvert_extrovert_letter.lower() not in last_question_dict.keys():
    introvert_extrovert_letter = input("Please enter a VALID corresponding letter: ")

if introvert_extrovert_letter.lower() == "d":
    introvert_extrovert_explanation = input("Help me understand: ")

# write last question and answer to the file
questionnaire_file.write(last_question + "\n\n")
questionnaire_file.write(last_question_dict[introvert_extrovert_letter])
if introvert_extrovert_explanation:
    questionnaire_file.write(", " + introvert_extrovert_explanation)

questionnaire_file.close()