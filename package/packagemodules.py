
#standard library
import math
print ("the value of sqrt is",math.sqrt(625))

#type of import
import math as u
print (u.cos)

#from
from math import tan
print(tan)

#all
from math import *
print ("the value is",sqrt(250))
print (sin)
print (cos)


#user define modules
import modulepackage
print (modulepackage.add(65,97,72,49))

import modulepackage as s
print (s.sub(34,56,86,29))

from modulepackage import multi
print (multi(45,27,17,24))

from modulepackage import *
print (div(45,63,21,17))

greeting ("morning")





