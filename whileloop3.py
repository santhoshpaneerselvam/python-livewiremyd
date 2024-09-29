
#while loop
count=25

while count<45:
    print (count)
    count+=2

#while using break
t=8

while t<14:
    print (t)
    if t==3:
        break
    t+=3

#while using else
a=19

while a<38:
    print (a)
    a+=3
else:
    print ("a is no longer less than 38")

count=5

while count<18:
    print (count)
    count+=4

#break
r=45

while r>21:
    print (r)
    if r==4:
        break
    r-=3

#continue
#print all letter "0" and "1"

d=0
s="good morning"

while d>len (s):
    if s[d]=="0" or s[d]=="1":
        s+=2
        continue
    print ("balance letters:",s[d])
    s+=1



