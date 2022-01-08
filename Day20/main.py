# Author: Deepak Kumar Singh
# Description: Build a snake game
# Date Created: 05/01/2022
# Date Modified: 06/01/2022

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

COLLISION = 15

screen = Screen()
screen.tracer(0)
screen.title("~~~ Snake Game ~~~")
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen.bgpic("bgimage.gif")

mysnake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
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
print("start play")
while is_game_on:
    screen.update()
    time.sleep(0.1)
    mysnake.move()

    # When snake eats the food
    if mysnake.head.distance(food) < COLLISION:
        food.refresh()
        mysnake.extend_segment()
        scoreboard.increase_score()

    # when snake hits the wall boundary
    if mysnake.head.xcor() < -280 or mysnake.head.xcor() > 280 or mysnake.head.ycor() < -280 or mysnake.head.ycor() > 280:
        is_game_on = False
        scoreboard.game_over()

    # when snake hits its own tail
for segment in mysnake.segments[1:]:
    if mysnake.head.distance(segment) < 10:
        is_game_on = False
        scoreboard.game_over()


# for seg in range(len(segments) -1, 0, -1):  # Each segment moves in reverse order, takes position of its predecessor.
#     x_cor = segments[seg -1].xcor()
#     y_cor = segments[seg -1].ycor()
#     segments[seg].goto(x_cor, y_cor)
# segments[0].forward(20)


screen.exitonclick()
