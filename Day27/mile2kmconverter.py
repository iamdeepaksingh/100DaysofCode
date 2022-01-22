# Author: Deepak Kumar Singh
# Description: Mile to KM Converter using Tkinter.
# Date Created: 21/01/2022
# Date Modified: 21/01/2022

from tkinter import *

FONT = ("Arial", 20, "bold")
VAL = 1.609344

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40)

# Now, lets create widgets



#Input
entry1 = Entry(width=10)
entry1.config(text="Enter Mile to convert")
entry1.grid(column=1, row=0)
#entry1.config(padx=40, pady=40)

#Labels

label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)
#label1.config(padx=40, pady=40)

label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)
#label2.config(padx=40, pady=40)

label3 = Label(text="KM", font=FONT)
label3.grid(column=2, row=1)
#label3.config(padx=40, pady=40)

label4 = Label(text="0", font=FONT)
label4.grid(column=1, row=1)
#label4.config(padx=40, pady=40)


#Button

def calc():
    mile = float(entry1.get())
    km = (mile * VAL)
    label4.config(text=km)



button1 = Button(text="Calculate", command=calc)
button1.grid(column=1, row=3)
button1.config(padx=40, pady=40)

window.mainloop()

