from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

in_game = True


def control():
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")
    s.onkey(exit_game, "q")


def exit_game():
    global in_game
    in_game = False


def check_edge():
    if snake.head.xcor() > 480 or snake.head.xcor() < - 480 or snake.head.ycor() > 400 or snake.head.ycor() < - 400:
        return True
    else:
        return False


def engine():
    global in_game
    while in_game:
        time.sleep(0.1)
        s.update()
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()

        if check_edge():
            score.reset()
            snake.reset()

        for segnment in snake.segments[1:]:
            if snake.head.distance(segnment) < 10:
                score.reset()
                snake.reset()


s = Screen()
s.screensize(600, 600)
s.tracer(0)
s.bgcolor("black")
s.title("Snake Game 🐍")

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
control()
engine()

score.game_over()
s.exitonclick()
