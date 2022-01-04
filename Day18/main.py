# Author: Deepak Kumar Singh
# Description: Day 18 of 100 days of code, Turtle graphics, Hirst Spot painting with colorgram
# Date Created: 02/01/2022
# Date Modified: 02/01/2022

import random
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
# tim.color("blue")
colors = ["dodger blue", "spring green", "green yellow", "tan", "magenta", "dark orange", "dark green",
          "brown", "aquamarine", "peru", "dark slate gray", "indian red"]

size = [i for i in range(10)]
direction = [0, 90, 180, 270]
tim.pensize(1)


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def draw_shape(no_sides):
    angle = 360 / no_sides
    for _ in range(no_sides):
        tim.forward(50)
        tim.right(angle)


# for shape_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side)

# def random_walk(width, speed, direction):
#     tim.pensize(width)
#     tim.speed(speed)
#     tim.setheading(random.choice(direction))
#
#
# for walk in range(200):
#     tim.color(random.choice(colors))
#     random_walk(10, 10, 10)

def random_walk():
    tim.speed(0)
    for _ in range(200):
        # tim.color(random.choice(colors))
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(direction))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size):
    tim.speed(0)
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(50)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)


# random_walk()

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
