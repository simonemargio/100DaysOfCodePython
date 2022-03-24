"""
Project Damien Hirst painting
"""

import colorgram
import turtle as t
import random

n_dots = 100
color = []

def check_color():
    extract_color = colorgram.extract("paint.jpg", 10)
    for current_color in extract_color:
        tuple = (current_color.rgb[0], current_color.rgb[1], current_color.rgb[2])
        color.append(tuple)

def initialize():
    t.colormode(255)
    brush.speed(0)
    brush.penup()
    brush.hideturtle()
    brush.setheading(225)
    brush.forward(300)
    brush.setheading(0)

def write_paint():
    for dot_count in range(1, n_dots + 1):
        brush.dot(20, random.choice(color))
        brush.forward(50)

        if dot_count % 10 == 0:
            brush.setheading(90)
            brush.forward(50)
            brush.setheading(180)
            brush.forward(500)
            brush.setheading(0)

check_color()
brush = t.Turtle()
initialize()
write_paint()

screen = t.Screen()
screen.exitonclick()