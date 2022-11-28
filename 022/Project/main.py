from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(800, 600)
s.title("Pong 🕹")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(r_paddle.move_up, "Up")
s.onkey(r_paddle.move_down, "Down")
s.onkey(l_paddle.move_up, "w")
s.onkey(l_paddle.move_down, "s")

in_game = True
while in_game:
    time.sleep(ball.ball_speed)
    s.update()
    ball.move()
    ball.check_collision_wall()
    ball.check_collision_paddle(r_paddle)
    ball.check_collision_paddle(l_paddle)
    ball.check_point(score)

s.exitonclick()
