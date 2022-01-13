# Author: Deepak Kumar Singh
# Description: Food class is used to track when the snake eats the food.
# Date Created: 07/01/2022
# Date Modified: 07/01/2022

from turtle import Turtle
import random
LOCATION_ON_AXIS = 280

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        new_x = random.randint(-LOCATION_ON_AXIS, LOCATION_ON_AXIS)
        new_y = random.randint(-LOCATION_ON_AXIS, LOCATION_ON_AXIS)
        self.goto(new_x, new_y)


