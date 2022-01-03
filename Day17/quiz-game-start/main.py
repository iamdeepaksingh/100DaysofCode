# Author: Deepak Kumar Singh
# Descr: Day 17 of 100 days of code. OOP n Python, making a quiz game
# Date Created: 01/01/2022
# Date Modified: 02/01/2022

from question_model import Question
from quiz_brain import Quiz
from data import question_data

question_bank = []
for q in question_data:
    text = q["question"]
    answer = q["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

print(question_bank[0].text)

play = Quiz(question_bank)
while play.still_has_questions():
    play.next_question()

print("You have completed the quiz")
print(f"Your final score was {play.score}/{play.question_no}")