import math as m
class Liczba:
    def __init__(self, value):
        self.value = value
        self.root = m.pow(value, 2)

    def __add__(self, liczba):
        return self.root + liczba.root


a = Liczba(3)
b = Liczba(3)
print(a+b)