
a=[3,6,9,12,15,18,21]
b=[4,8,12,16,20,24,24]
x=[]
y=[]
for s in range(7):
    if s%2==0:
        y.append(b[s])
    else:
        x.append(a[s])
print(x,y)
x.extend(y)
print(x)

        

