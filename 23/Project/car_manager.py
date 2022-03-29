from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car = []
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        for i in range(0,10):
            new_car = self.setting_car()
            self.car.append(new_car)

    def add_new_car(self):
        new_car = self.setting_car()
        self.car.append(new_car)

    def update_level(self):
        self.add_new_car()
        self.speed += MOVE_INCREMENT

    def setting_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, random.randint(2, 3), 1)
        new_car.left(180)
        new_car.goto(random.randint(300, 800), random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        return new_car

    def move(self):
        for i in range(0, len(self.car)):
            self.car[i].forward(self.speed)
            self.check_car_end_board(i)

    def check_car_end_board(self, current_car):
        if self.car[current_car].xcor() < - 320:
            self.car[current_car].goto(random.randint(300, 800), random.randint(-250, 250))

    def check_collision(self, player):
        for i in range(0, len(self.car)):
            if self.car[i].distance(player) < 25:
                return True
