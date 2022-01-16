# Author: Deepak Kumar Singh
# Description: U.S states quiz using Turtle and Pandas
# Date Created: 15/01/2022
# Date Modified: 15/01/2022

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S State Quiz")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

data = pd.read_csv("50_states.csv")

guessed_states = []
total_states = len(data.state)
current_state = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{current_state}/{total_states} states correct", prompt="What's another state? ").title()
    current_state += 1
    if answer_state == "X" or current_state == total_states:
        game_is_on = False
    if answer_state in list(data['state']):
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item(), align="center", font=("Arial", 8, "normal"))


# The states which could not be guessed by users should be written to the text file.
states_to_learn = data.loc[~data.state.isin(guessed_states)]
states_to_learn.state.to_csv("states_to_learn.csv")


turtle.mainloop()

