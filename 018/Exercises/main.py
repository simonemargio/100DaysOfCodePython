import turtle as t
import random

def sqare():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def dashedLine():
    for _ in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def geometric():
    distance = 100
    for sides in range(3,11):
        angle = round(360 / sides)
        turtle.color(randomColor())
        while sides != 0:
            turtle.forward(distance)
            turtle.right(angle)
            sides -= 1

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

move = [0, 90, 180, 270]
def randomPath():
    turtle.hideturtle()
    turtle.speed(0)
    for _ in range(100):
        turtle.color(randomColor())
        turtle.pensize(10)
        turtle.forward(40)
        turtle.right(random.choice(move))

def spirograph():
    turtle.hideturtle()
    turtle.speed(0)
    for _ in range(int(360 / 5)):
        turtle.color(randomColor())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + 5)


turtle = t.Turtle()
t.colormode(255)
spirograph()



screen = t.Screen()
screen.exitonclick()