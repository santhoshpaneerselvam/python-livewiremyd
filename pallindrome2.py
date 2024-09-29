

num=int(input("enter the value:"))
num1=num
h=0

while num1 >0:
    h=(h*10)+num1%10
    num1//=10
    
print(h)
print(num)

num=int(input("enter the value"))
value=num
t=0

while num >0:
    t=(t*10)+num%10
    num//=10
    print (t)

if (value==h):
    print ("value is equal to pallindrome")
    print ("t is pallindrome")
else:
    print ("is not pallindrome")

    
