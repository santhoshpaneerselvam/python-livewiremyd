'''
import math
class Cuboid :
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
    def volume (self):
        return self.length*self.width*self.height
    
    def surfacearea (self):
        return 2*(self.length*self.width+self.width*self.height+self.height*self.length)
    
    def spacediagonal (self):
        return math.sqrt(self.length**2+self.width**2+self.height**2)
    
length=8
width=6
height=4
cuboid= Cuboid(length,width,height)
volume= cuboid.volume()
surfacearea= cuboid.surfacearea()
spacediagonal= cuboid.spacediagonal()

print ("volume of cuboid:",volume)
print ("surface area of cuboid:",surfacearea)
print ("spacediagonal of cuboid:",spacediagonal)

                                                
#Area and diagonal of hexagon
import math
def hexagonArea(s):
    return ((3*math.sqrt(3)*(s*s))/2)
if __name__=="__main__":
    s=5
    print ("Area;","{0:.5f}".format(hexagonArea(s)))

'''
from math import sqrt
def hexadiagonal(d):
    return (3*sqrt(3)*pow(d,3))/7
d=15
print ("area of hexagon:",round(hexadiagonal(d),5))


