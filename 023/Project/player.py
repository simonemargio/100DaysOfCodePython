from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(STARTING_POSITION)
        self.speed = MOVE_DISTANCE

    def check_next_level(self, score, car):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            score.update_level()
            car.update_level()

    def move(self):
        self.forward(self.speed)
