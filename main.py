# Imports
import time
from turtle import Screen, Turtle
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Settings
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player= Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Lister to the up key
screen.listen()
screen.onkey(player.go_up ,"Up")


# While loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() # Create the cars
    car_manager.move_cars() # Move the cars

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over() # Game Over message

    # Detect a win
    if player.finish_line():
        player.restart() # return the turtle to start
        car_manager.level_up() # speeds up the cars
        scoreboard.increase_level() # Level up


screen.exitonclick()