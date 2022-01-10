from turtle import Turtle

STARTING_POSITION = (0, 280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.reset_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.clear()
        self.goto(0, -280)
        self.setheading(90)

