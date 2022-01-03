# Author: Deepak Kumar Singh
# Descr: Python OOP , Day 16
# Date Created: 31/12/2021
# Date Modified: 31/12/2021
from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()

table.add_column("Name", ["Deepak","Sachin", "Rahul"])
table.add_column("Name2", ["Deepak","Sachin", "Rahul"])
table.align = 'r'
print(table)