
from math import pi

class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return "i am a two dimensional shape"
    def __str__(self):
        return self.name


class square(shape):
    def __init__(self,length):
        super().__init__("length")
        self.length=length
    def area (self):
        return self.length**2
    def fact(self):
        return "square have each angle equal to 90 degrees"


class circle(shape):
    def __init__(self,radius):
        super().__init__("radius")
        self.radius=radius
    def area (self):
        return pi*self.radius**2


a=square(4)
b=circle(7)
print (a)
print (a.area())
print (a.fact())
print (b)
print (b.area())
print (b.fact())



