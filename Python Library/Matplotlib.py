
""" import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,4,8,12])
ypoints=np.array([0,145,30,90])
plt.plot(xpoints,ypoints)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([2,6,9,13])
ypoints=np.array([4,7,1,10])
plt.plot(xpoints,ypoints)
plt.title("SEASON")
plt.xlabel("RAIN SEASON")
plt.ylabel("SUMMER SEASON")
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7,14,6,17])
plt.plot(ypoints)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,15,7,18,4])
plt.plot(ypoints,marker='o',ms=20)
plt.plot(ypoints,marker='*',ms=20)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,4,14])
plt.plot(ypoints,'*:b',ms=20)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,4,14,7])
plt.plot(ypoints,marker='o',ms=15)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,4,14,7])
plt.plot(ypoints,marker='o',ms=25,mec='r',mfc='g')
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,4,14,7])
plt.plot(ypoints,marker='*',ms=20,mfc='r',mec='b')
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,8,1,10,4,14,7])
plt.plot(ypoints,color='r',marker='*',ms=25)
plt.show()
plt.plot(ypoints,c="hotpink",marker='o',ms=25)
plt.show()
plt.plot(ypoints,linewidth='20.5')
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
y1=np.array([2,8,4,12,1,14,7])
y2=np.array([7,2,9,3,15,5,18])
plt.plot(y1,marker='o',ms=25,mfc='b',mec='y')
plt.plot(y2,marker='*',ms=25,mfc='r',mec='g')
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0,1,2,3,4,5])
y1=np.array([2,8,1,10,4,15])
x2=np.array([0,1,2,3,4,5])
y2=np.array([7,2,9,3,15,5])
plt.plot(x1,y1,x2,y2)
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np 
x=np.array([80,85,90,95,100,105,110,115,120,125,130,135])
y=np.array([240,250,260,270,280,290,300,310,320,330,340,350])
plt.plot(x,y,marker='*',ms=20,mec='b',mfc='r')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show() """


""" import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,85,90,95,100,105,110,115,120,125,130,135])
y=np.array([240,250,260,270,280,290,300,310,320,330,340,350])

font1={'family':'serif','color':'Green','size':20}
font2={'family':'serif','color':'Red','size':15}
plt.title("Sport Watch Data",fontdict=font1)
plt.xlabel("Average Pulse",fontdict=font2)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.plot(x,y,marker='o',ms=15,mec='green',mfc='orange')
plt.show() """


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
np.random.seed(45)
x= np.random.rand(50) * 10
y= 2 * x + 1 + np.random.randn(50) * 2
slope,intercept,r_value,p_value,std_err = linregress(x,y)
y_pred=slope * x + intercept
plt.scatter(x,y,label ='Data')
plt.plot(x,y_pred,color='red',label=f'Regression line:y={slope:.5f}x + {intercept:.5f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()



