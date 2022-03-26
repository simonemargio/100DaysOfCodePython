from snake import Snake
from turtle import Screen
import time

in_Game = True

def initialize_screen():
    s = Screen()
    s.screensize(600, 600)
    s.tracer(0)
    s.bgcolor("black")
    s.title("Snake Game 🐍")
    return s

def engine():
    while in_Game:
        time.sleep(0.1)
        screen.update()
        snake.move()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")


screen = initialize_screen()
snake = Snake()
screen.listen()
engine()

screen.exitonclick()
