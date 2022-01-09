# Author: Deepak Kumar Singh
# Description: Car Manager class
# Date Created: 09/01/2022
# Date Modified: 09/01/2022

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create

    def create(self):
        self.shape("square")
        self.penup()
        self.color("white")
        # self.shapesize(stretch_wid=2, stretch_len=1)
        self.goto(280, 100)
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
