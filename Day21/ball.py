# Author: Deepak Kumar Singh
# Description: Ball class
# Date Created: 08/01/2022
# Date Modified: 08/01/2022

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        # self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # Top or bottom bouncing along y axis

    def bounce_x(self):
        self.x_move *= -1  # left or right bouncing along x axis
        self.move_speed *= 0.9  # When paddle hits the ball, ball speed should increase.

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



