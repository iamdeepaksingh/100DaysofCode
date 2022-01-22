# Author: Deepak Kumar Singh
# Description: Tkinter GUI, positional arguments and keyword arguments. *args (tuples) and **kwargs (dictionary)
# Date Created: 21/01/2022
# Date Modified: 21/01/2022

from tkinter import *

FONT=("Arial", 18, "bold")
window = Tk()
window.title("GUI Program")
window.minsize(height=600, width=500)
window.config(padx=20, pady=20)

#label
label1 = Label(text="label1", font =FONT)
label1.pack()

def button_clicked():
    new_label = entry.get()
    label1.config(text=new_label)

#Button
button1 = Button(text="Click me", command=button_clicked)
button1.pack()

#input
entry = Entry(width=10)
entry.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "example of multiline entry")
print(text.get("1.0", END))
text.pack()

#spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbox
def checked_button():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="is on?", variable=checked_state, command=checked_button)
checked_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used )
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used )
radiobutton1.pack()
radiobutton2.pack()



#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apples", "Grapes", "Orange", "Strawberry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# 3 layout managers. pack (stacked one after another), place(coordinates x and y) and grid (rows and columns)


window.mainloop()