# Imports
import random
from turtle import  Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        'ran_chance' will create a 'car' in a chance of 1/6
        :return: A square double len, random color, random position on Y (-250, 250)
        """
        ran_chance = random.randint(1, 6)
        if ran_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Moves the cars
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
         When winning a game, the car speed goes up by 2
        """
        self.car_speed += MOVE_INCREMENT