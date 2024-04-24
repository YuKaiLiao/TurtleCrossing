from turtle import Turtle
from car import Car
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.random_manager = Random()
        self.cars = []
        # car = Car(random_manager.choice(COLORS), (270, random_manager.randrange(-250, 250, 10)))
        # self.cars.append(car)
        for i in range(300):
            self.move_all()

            if i % 10 == 0:
                self.add_new_car()

    def move_all(self):
        for i in self.cars:
            i.move(STARTING_MOVE_DISTANCE)

    def add_new_car(self):
        if len(self.cars) > 0:
            last_car = self.cars[-1]
            if last_car.xcor() > 250:
                return
        car = Car(self.random_manager.choice(COLORS), (270, self.random_manager.randrange(-250, 250, 10)))
        self.cars.append(car)
