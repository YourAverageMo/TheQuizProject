import os

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def sclr():
    os.system("clear")


question_bank = []
for q in question_data:
    text = q["text"]
    answer = q["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    sclr()
    quiz.new_question()
    quiz.check_answer()
    input(
        f"Your Current score is: {quiz.score}. Press enter to go to the next question...")

sclr()
print("You've completed the quiz. hope that wasnt too hard!")
print(f"Your final score was {quiz.score}")
