# Author: Deepak Kumar Singh
# Description: Build a snake game
# Date Created: 05/01/2022
# Date Modified: 06/01/2022

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.tracer(0)
screen.title("~~~ Snake Game ~~~")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen.bgpic("bgimage.gif")

mysnake = Snake()
screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down,"Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")

# x_pos = [-40, -20, 0]


is_game_on = True
# segments = []

# for i in range(3):
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     # new_segment.speed(1)
#     new_segment.goto(x_pos[i], 0)
#     segments.append(new_segment)



while is_game_on:
    screen.update()
    time.sleep(0.1)

    mysnake.move()

    # for seg in range(len(segments) -1, 0, -1):  # Each segment moves in reverse order, takes position of its predecessor.
    #     x_cor = segments[seg -1].xcor()
    #     y_cor = segments[seg -1].ycor()
    #     segments[seg].goto(x_cor, y_cor)
    # segments[0].forward(20)





screen.exitonclick()