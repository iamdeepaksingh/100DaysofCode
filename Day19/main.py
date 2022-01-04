# Author: Deepak Kumar Singh
# Description: Turtle race game in python.
# Date Created: 04/01/2022
# Date Modified: 04/01/2022

from turtle import Turtle, Screen
import random
new_turtle = Turtle(shape="turtle")

colors = ["violet", "blue", "green", "yellow", "orange", "red"]
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make a bet", prompt="Choose your turtle")
# print(user_choice)

x_shift = 230
y_shift = [-70, -40, 10, 40, 70, 100]

is_race_on = False
turtle_list = []

if user_choice:
    is_race_on = True

for c in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[c])
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(x=-x_shift, y=y_shift[c])
    turtle_list.append(new_turtle)

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle.lower() == user_choice.lower():
                print(f"You have won! Winning turtle is {winning_turtle}")
            else:
                print(f"You lost, Winning turtle is {winning_turtle}")
        distance = random.randint(0, 10)
        turtle.forward(distance)


# tim.penup()
# tim.color(user_choice)
# tim.goto(x=-230, y=-100)

screen.exitonclick()