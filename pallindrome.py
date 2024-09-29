

num=int(input("enter the value:"))
value=num
a=0
while num>0:
    a=(a*10)+num%10
    num//=10
    print (a)

if(value==a):
    print ("value is equal to num")
    print ("a is pallindrome")
else:
    print ("is not pallindrome")
