
# # NumPy is a Python library used for working with arrays.
# # It also has functions for working in domain of linear algebra, fourier transform, and matrices.
'''
import numpy
arr=numpy.array([21,22,23,24,25,26,27,28,29,30])
print(arr)
print(arr[5])
print(arr[3] + arr[8])
print(arr[5:9])
print(arr[6:])
print(arr[:5])
print(arr[-7:-3])
print(arr[1:10:3])

import numpy as np
arr=np.array([17,15,13,11,19])
print(arr)
a=[]
print(type(a))
print(type(arr))
'''
""" import numpy as np
print(np.__version__)

arr=np.array([[45,46,47],[48,49,50],[51,52,53]])
print(arr)
print('2nd element on 1st now:',arr[0,1])
print('elements:',arr[2,1]) """

""" import numpy as np
arr=np.array([[81,82,83,84,85],[86,87,88,89,90]])
print(arr[1,4])
print("1.",arr[1,1:4])
print("2.",arr[0:3,2])
print("3.",arr[1:2,2:3]) """

import numpy as np
arr=np.array([[[31,32,33],[34,35,36],[37,38,39],[40,41,42]]])
print("4.",arr)
print("5.",arr[0,1,2])
