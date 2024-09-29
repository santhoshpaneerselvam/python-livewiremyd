
#Pandas is a python library used for working with datasets.
#It has funtions for analyzing,cleaning,exploringa and manipulating data.

import pandas as pd
k=[7,3,5]
myvar=pd.Series(k)
print(myvar)

import pandas as pd
t=[4,6,8]
myvar=pd.Series(t,index=["a","b","c"])
print(myvar)

'''
import pandas as pd
mydataset={
    'bikes':["Pulsar","Duke","RN5"],
    'passings':[7,5,3]
}
print (mydataset)
myvar=pd.DataFrame(mydataset)
print(myvar)

'''
