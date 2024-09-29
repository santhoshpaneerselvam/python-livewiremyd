
""" import pandas as pd
t=[9,7,5,3,1,8,6,4,2]
myvar=pd.Series(t)
print (myvar) """


""" import pandas as pd
k=[15,17,19,21,23,25]
myvar=pd.Series(k,index=["a","b","c","d","e","f"])
print(myvar) """

import pandas as pd
mydataset={
    'Fruits':["Apple","Mango","Orange","Banana","Grapes","Pineapple","Watermelon"],
    'Vegetables':["Tomato","Potato","Carrot","Beetroot","Cabbage","Cucumber","Raddish"]
}
print (mydataset)
myvar=pd.DataFrame(mydataset)
print (myvar)
