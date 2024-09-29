""" import math
def hexagonArea(t):
    return((3*math.sqrt(3)*(t*t))/2);
if __name__=="__main__":
    t=4
    print("Area:","{0:.4f}".format(hexagonArea(t))) 
 """

from math import sqrt
def hexadiagonal(d):
    return(3*sqrt(3)*pow(d,2))/8
d=10
print("area of hexagon:",round(hexadiagonal(d),3))