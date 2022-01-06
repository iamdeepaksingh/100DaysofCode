# Author: Deepak Kumar Singh
# Description: Build a snake game
# Date Created: 06/01/2022
# Date Modified: 06/01/2022

from turtle import Turtle

X_POS = [-40, -20, 0]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            # new_segment.speed(1)
            new_segment.goto(X_POS[i], 0)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0,
                         -1):  # Each segment moves in reverse order, takes position of its predecessor.
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
        # self.forward(MOVE_DISTANCE)

    def down(self):
        self.head.setheading(270)
        # self.forward(MOVE_DISTANCE)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
