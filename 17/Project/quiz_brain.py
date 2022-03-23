class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.questions_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong.\nThe correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{len(self.questions_list)}\n")

    def finish(self):
        print(f"You've completed the quiz!\nFinal score: {self.score}/{len(self.questions_list)}")

    def next_question(self):
        new_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {new_question.text} (True/False)?:")
        self.check_answer(user_answer, new_question.answer)