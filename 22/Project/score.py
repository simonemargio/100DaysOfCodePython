from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.scoreboard()

    def scoreboard(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, align="center", font=("Courier", 80, "normal"))

    def update_score(self, paddle):
        if paddle == 1:
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.scoreboard()
