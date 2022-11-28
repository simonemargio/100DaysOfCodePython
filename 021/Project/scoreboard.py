from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-430, 380)
        self.hideturtle()
        self.color("white")
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("Game over! 🫡", False, align="center", font=("Arial", 20, "normal"))
