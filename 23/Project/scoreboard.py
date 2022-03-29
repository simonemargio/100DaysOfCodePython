from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(- 230, 270)
        self.current_level = 1
        self.level()

    def level(self):
        self.write(f"Level: {self.current_level}", False, align="center", font=FONT)

    def update_level(self):
        self.current_level += 1
        self.clear()
        self.level()

    def end(self):
        self.home()
        self.write("Game over! 🫡", False, align="center", font=FONT)