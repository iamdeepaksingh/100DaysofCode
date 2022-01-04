# Author: Deepak Kumar Singh
# Description: Sketch app using Turtle package in python.
# Date Created: 04/01/2022
# Date Modified: 04/01/2022

from turtle import Turtle, Screen
tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def move_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # tim.forward(50)


def move_anticlockwise():
    tim.setheading(tim.heading() - 10)
    # tim.forward(50)

def clear_turtle_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()


screen.onkey(key = "w", fun = move_forward) # Higher order functions, functions that work with other functions.
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_clockwise)
screen.onkey(key = "d", fun = move_anticlockwise)
screen.onkey(clear_turtle_drawing, "c")

screen.exitonclick()