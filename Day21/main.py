# Author: Deepak Kumar Singh
# Description: Pong game - Day21 - 100 Days of code
# Date Created: 08/01/2022
# Date Modified: 08/01/2022

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import  Scoreboard

screen = Screen()
screen.tracer(0)  # Turn off animation
screen.setup(width=800, height=600)
screen.title(titlestring="Pong Game")
screen.bgcolor("black")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# ball.move()

# paddle = Turtle()
# # paddle.hideturtle()
# paddle.penup()
# paddle.shape("square")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.color("white")
# paddle.goto(350, 0)


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check collision with top or bottom Y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check collision with left or right along x axis
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()