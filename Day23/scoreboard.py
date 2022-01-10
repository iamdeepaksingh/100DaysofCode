# Author: Deepak Kumar Singh
# Description: Scoreboard class
# Date Created: 10/01/2022
# Date Modified: 10/01/2022

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_num = 0
        self.score = 0
        self.create()

    def create(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-200, 200)
        self.write(f"Level {self.score}", align="center", font=FONT)

    def refresh(self):
        self.clear()
        self.level_num += 1
        self.score += 1
        self.write(f"Level {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=FONT)


