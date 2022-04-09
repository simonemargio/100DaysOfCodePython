from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(self.window, text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.image_false = PhotoImage(file="images/false.png")
        self.image_true = PhotoImage(file="images/true.png")

        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.false_pressed)
        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.true_pressed)

        self.button_false.grid(row=2, column=0)
        self.button_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score:{self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, true_false):
        if true_false:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
