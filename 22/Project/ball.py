from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.home()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def check_collision_wall(self):
        if self.ycor() < -280 or self.ycor() > 280:
            self.y_move *= -1

    def check_collision_paddle(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < - 320):
            self.x_move *= -1
            self.ball_speed *= 0.9

    def check_point(self, s):
        if self.xcor() > 390 or self.xcor() < - 390:
            if self.xcor() > 390:
                s.update_score(1)
            else:
                s.update_score(2)
            self.ball_speed = 0.1
            self.home()
            self.x_move *= -1
