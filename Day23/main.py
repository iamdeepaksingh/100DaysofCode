# Author: Deepak Kumar Singh
# Description: Day23 of 100 days of code - Turtle crossing game
# Date Created: 09/01/2021
# Date Modified: 09/01/2021

from turtle import Turtle, Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
car = CarManager(6)
player = Player()
scoreboard = Scoreboard()


screen.title("Turtle Crossing Game")
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.listen()
screen.onkey(player.go_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    for c in car.carlist:
        if c.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False
        if c.xcor() < -280:
            car.reset_position(c)
        if player.ycor() > 280:
            scoreboard.refresh()
            car.level_up()
            player.reset_position()


screen.exitonclick()