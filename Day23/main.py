# Author: Deepak Kumar Singh
# Description: Day23 of 100 days of code - Turtle crossing game
# Date Created: 09/01/2021
# Date Modified: 09/01/2021

from turtle import Turtle, Screen
import time
from car_manager import CarManager

screen = Screen()
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.setup(height=600, width=600)
screen.bgcolor("black")
car = CarManager()


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.move()


screen.exitonclick()