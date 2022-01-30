# Author: Deepak Kumar Singh
# Descr: Day 17 of 100 days of code. OOP in Python, making a quiz game
#  Questions are generated based on API calls from Open Trivia Database.
# TKinter is used for the GUI part.
# Date Created: 01/01/2022
# Date Modified: 31/01/2022

from ui import QuizInterface
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for q in question_data:
    text = q["question"]
    answer = q["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

#print(question_bank[0].text)

quiz = QuizBrain(question_bank)
# while play.still_has_questions():
#     play.next_question()

quiz_ui = QuizInterface(quiz)

#print("You have completed the quiz")
#print(f"Your final score was {quiz.score}/{quiz.question_no}")