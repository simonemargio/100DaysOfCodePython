import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.title("Turtle crossing road 🐢")
s.tracer(0)
s.listen()

p = Player()
car = CarManager()
level = Scoreboard()
s.onkey(p.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    p.check_next_level(level, car)
    car.move()
    collision = car.check_collision(p)
    if collision:
        game_is_on = False

level.end()
s.exitonclick()
