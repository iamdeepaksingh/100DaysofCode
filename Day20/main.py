# Author: Deepak Kumar Singh
# Description: Build a snake game
# Date Created: 05/01/2022
# Date Modified: 05/01/2022

from turtle import Turtle, Screen
import time
screen = Screen()
screen.tracer(0)
screen.title("~~~ Snake Game ~~~")
screen.setup(width=600, height=600)
screen.bgcolor("black")

x_pos = [-40, -20, 0]


is_game_on = True
segments = []

for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    # new_segment.speed(1)
    new_segment.goto(x_pos[i], 0)
    segments.append(new_segment)


while is_game_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        if seg.xcor() > 280:
            is_game_on = False
        # seg.penup()
        seg.forward(20)



screen.exitonclick()