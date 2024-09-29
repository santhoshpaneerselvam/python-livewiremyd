
import math
class hexagon:
	def __init__(self,height,perimeter,length):
		
		self.height=height
		self.perimeter=perimeter
		self.length=length
	def areaofhexagon(self):
		return ( (6*self.perimeter*self.height) + (3 *(3) *self.perimeter *self.length))
	def angle(self):
		return "hexagon have equal to angle of 720 degrees"


length=6
perimeter=8
height=4

hexagon=hexagon(height,perimeter,length)
areaofhexagon= hexagon.areaofhexagon()
angle=hexagon.angle()

print("area of hexagon :",areaofhexagon)
print ("angle of hexagon:",angle)

'''
import math
class Cuboid:
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
width=5
height=4

cuboid= Cuboid(length,width,height)
volume= cuboid.volume()
surfacearea= cuboid.surfacearea()
spacediagonal= cuboid.spacediagonal()

print ("volume of cuboid:",volume)
print ("surface area of cuboid:",surfacearea)
print ("spacediagonal of cuboid:",spacediagonal)

'''



		
