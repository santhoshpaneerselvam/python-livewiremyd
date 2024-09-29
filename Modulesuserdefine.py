
#standard library
import math
print ("the value of sqrt is",math.sqrt(64))

#type of import
import math as m
print (m.pi)

#from
from math import pi
print (pi)

#all
from math import *
print ("the value is",sqrt(144))
print (pi)
print (tanh)


#user define modules
import Modules
print (Modules.add(5,8,10,7))

import Modules as m
print (m.add(56,43,67,23))

from Modules import add
print (add(76,94,36,40))

from Modules import *
print (sub(52,87))

greeting("all")




