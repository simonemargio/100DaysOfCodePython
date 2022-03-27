from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time


def initialize_screen():
    s = Screen()
    s.screensize(600, 600)
    s.tracer(0)
    s.bgcolor("black")
    s.title("Snake Game 🐍")
    return s


def control():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def check_edge():
    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        return True
    else:
        return False


def engine():
    in_game = True
    while in_game:
        time.sleep(0.1)
        screen.update()
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()

        if check_edge():
            in_game = False

        for segnment in snake.segments[1:]:
            if snake.head.distance(segnment) < 10:
                in_game = False


screen = initialize_screen()
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
control()
engine()
score.game_over()
screen.exitonclick()
