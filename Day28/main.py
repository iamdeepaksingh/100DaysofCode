# Author: Deepak Kumar Singh
# Description: Pomodoro using tkinter
# Date Created: 22/01/2022
# Date Modified: 22/01/2022

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    marks = ""
    global reps
    reps = 0
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def call_timer():
    work_Sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    if reps % 2 == 1:
        count_down(work_Sec)
        title_label.config(text="Work", fg=GREEN)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Rest", fg=RED)




    #count_down(1*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
        # Example of dynamic typed, count_sec was integer and now holding string. Python is also strongly typed.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        #  This means after 1 sec, call count_down function and pass count-1 as parameter.
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        call_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in work_sessions:
            marks += "✅"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(column=1, row=1)
#count_down(5)

# Labels and Buttons

start_button = Button(text="Start",  highlightthickness=0, command=call_timer)
start_button.grid(column=0, row=3)


reset_button = Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, highlightthickness=0, font=("Arial", 50, "bold"))
title_label.grid(column=1, row=0)

check_mark = Label(highlightthickness=0)
check_mark.grid(column=1, row=4)

window.mainloop()