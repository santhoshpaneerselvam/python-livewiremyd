
#while loop
count=3
while count<58:
    print (count)
    count+=4

#while using break
t=20
while t<40:
    print (t)
    if t==2:
      break
    t+=2

#while using else
s=25
while s<56:
    print (s)
    s+=2

else:
    print ("s is no greater less than 56")

count=10
while count<20:
    print (count)
    count+=2

#break
d=42
while d>23:
    print (d)
    if d==5:
        break
    d-=1

#continue
#print all letter except '0' and 'n'
g=0
h="good morning"
while g<len(h):
    if h[g]=='o' or h[g]=='n':
        g+=1
        continue
    print('balance letter:',h[g])
    g+=1
    
        
      
           
    
