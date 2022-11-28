"""
Exercise Etch-A-Sketch
"""

from turtle import Turtle, Screen


def initialize_screen():
    return Screen()


def initialize_turtle():
    return Turtle()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_right():
    t.right(10)


def move_left():
    t.left(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t = initialize_turtle()
s = initialize_screen()
s.listen()

s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(move_left,"a")
s.onkey(move_right,"d")
s.onkey(clear,"c")


s.exitonclick()