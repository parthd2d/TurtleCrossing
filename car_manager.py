from turtle import Turtle
from random import randint

INITIAL_MOVE_DISTANCE = 10
INCREMENT_SPEED = 5
BACKGROUND_COLOR = "white"
MAXIMUM_DISTANCE = (400,400)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def random_y_cor():
    ycor = -230 + (randint(1, 12) - 1) * 40
    return ycor


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = INITIAL_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 6:
            new_car = Turtle("square")
            new_car.color(random_color())
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(300, random_y_cor())
            for car in self.all_cars:
                if new_car.distance(car) < 40:
                    new_car.goto(MAXIMUM_DISTANCE)
                    del new_car
                    break
            else:
                self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT_SPEED
