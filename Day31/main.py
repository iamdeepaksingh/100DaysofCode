# Author: Deepak Kumar Singh
# Description: Flash card for language learning using TKinter.
# Date Created: 24/01/2022
# Date Modified: 24/01/2022

from tkinter import *
from tkinter import Canvas
import pandas as pd
import random
import time
current_card = {}

BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    #original_df = pd.read_csv("./data/french_words.csv")
    original_df = pd.read_csv("./data/dutch.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

# ----------------------- Logic ----------------------- #

def get_nextcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['Dutch'], fill="black")
    canvas.itemconfig(card_title, text='Dutch', fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    get_nextcard()

# ----------------------- UI Setup ----------------------- #

window = Tk()
window.title("Learn a language - Linguas")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(height=400, width=500)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating widgets
cross_img = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=get_nextcard)
cross_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img , highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

get_nextcard()


window.mainloop()







