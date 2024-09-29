
import math
class cuboid:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
    def volume(self):
        return(self.length*self.width*self.height)
    def surfacearea(self):
        return 2*(self.length*self.width+self.width* self.height+self.height*self.length)  
    def diagonal(self):
        return math.sqrt(self.length**2 + self.width**2+self.height**2)

length=7
width=4
height=5

cuboid=cuboid(length,width,height)
volume= cuboid.volume()
surfacearea=cuboid.surfacearea()
diagonal= cuboid.diagonal()

print("volume cuboid:",volume)
print("surfacearea:",surfacearea)
print("diagonal cuboid:",diagonal)