# Author: Deepak Kumar Singh
# Description: Build a snake game. Class Inheritance is the process of inheriting methods from the class.
# Date Created: 06/01/2022
# Date Modified: 12/01/2022

from turtle import Turtle

STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0,
                         -1):  # Each segment moves in reverse order, takes position of its predecessor.
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.setheading != DOWN:
            self.head.setheading(UP)
        # self.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.setheading != UP:
            self.head.setheading(DOWN)
        # self.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
