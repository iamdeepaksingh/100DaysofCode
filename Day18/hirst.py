# Author: Deepak Kumar Singh
# Description: Hirst painting using colorgram.py
# Date Created: 03/01/2022
# Date Modified: 03/01/2022

# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
#
# color_list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
#
# print(color_list)

import turtle as t
import random

list_of_color = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]
tim = t.Turtle()
tim.shape("arrow")
t.colormode(255)

tim.setheading(225)
tim.forward(350)
tim.setheading(0)


def change_direction():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


def draw_straight_dots():
    for i in range(10):
        tim.dot(20, random.choice(list_of_color))
        tim.fd(50)


for j in range(11):
    draw_straight_dots()
    change_direction()


screen = t.Screen()
screen.exitonclick()



