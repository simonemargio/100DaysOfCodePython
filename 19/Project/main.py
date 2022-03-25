"""
Project Turtle race
"""
from tkinter import messagebox
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def initialize_screen():
    s = Screen()
    s.setup(500, 400)
    return s


def initialize_turtle():
    return Turtle(shape="turtle")


def input_turtle_name():
    user_choise = ""
    while not user_choise in colors:
        user_choise = s.textinput("Make your bet", "Witch turtle will win the race? Enter a color:")

    return user_choise


def create_turtle():
    turtle = []
    for color in colors:
        t = initialize_turtle()
        t.penup()
        t.color(color)
        turtle.append(t)
    return turtle


def set_turtle():
    y = -100
    for i in range(len(t)):
        t[i].goto(-230, y)
        y += 50


def start_turtle_race():
    while True:
        for turtle in t:
            x = turtle.xcor()
            if x >= 210:
                return turtle.color()
            turtle.forward(random.randint(1, 10))
        s.delay(20)


def check_win():
    if win_turtle[0] == user_turtle:
        messagebox.showinfo("Yeah", "You win! 🥳")
    else:
        messagebox.showinfo("Oh no", "Sorry, you lose. 😞")


s = initialize_screen()
t = create_turtle()
set_turtle()
user_turtle = input_turtle_name()
win_turtle = start_turtle_race()

check_win()

s.exitonclick()
