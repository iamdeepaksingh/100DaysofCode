# Author: Deepak Kumar Singh
# Description: Scoreboard class is used to track score when the snake eats the food or hits the wall.
# Date Created: 07/01/2022
# Date Modified: 12/01/2022

from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        # self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh_score()
        self.write_high_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def get_high_score(self):
        with open("data.txt", "r") as f:
            self.high_score = int(f.read())

    def write_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.high_score))


