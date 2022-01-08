# Author: Deepak Kumar Singh
# Description: Class Inheritance is the process of inheriting methods from the class.
# Date Created: 07/01/2022
# Date Modified: 07/01/2022

class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("breathe in , breathe out")


class Fish(Animal):  # Class Fish inherits from class Animal.
    def __init__(self):
        super()

    def breathe(self):
        super().breathe()
        print("But underwater")

    def swim(self):
        print("I can swim")

kia = Fish()

kia.swim()
kia.breathe()