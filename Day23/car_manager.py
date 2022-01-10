# Author: Deepak Kumar Singh
# Description: Car Manager class
# Date Created: 09/01/2022
# Date Modified: 09/01/2022

import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, num_of_cars):
        super().__init__()
        self.carlist = []
        self.ypos = 240
        self.timer = 0.1
        self.new_x = 0
        self.new_y = 0
        self.create(num_of_cars)

    def create(self, num_of_cars):
        for car in range(num_of_cars):
            seg = Turtle("square")
            #self.shape("square")
            seg.penup()
            seg.shapesize(stretch_wid=1, stretch_len=2)
            seg.color(random.choice(COLORS))
            seg.goto(260, self.ypos)
            self.ypos -= 90
            self.carlist.append(seg)

    def move(self):
        for car in range(0, len(self.carlist)):
            time.sleep(self.timer)
            self.new_x = self.carlist[car].xcor() - (STARTING_MOVE_DISTANCE*random.randint(1, 10))
            self.new_y = self.carlist[car].ycor()
            self.carlist[car].goto(self.new_x, self.new_y)

    def reset_position(self, obj):
        ypos2 = obj.ycor()
        obj.goto(240, ypos2)

    def level_up(self):
        self.new_x -= MOVE_INCREMENT  # needs some improvement here.
        # self.timer = 0.05



