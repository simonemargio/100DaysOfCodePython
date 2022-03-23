from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for single_question in question_data:
    question = Question(single_question["question"], single_question["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.finish()