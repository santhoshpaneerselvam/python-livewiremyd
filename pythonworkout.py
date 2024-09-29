
#Adam Number
def reversedigit(num):
    t=0
    while (num >0):
        t=(t*10)+num%10
        num//=10
        return t

def square (num):
    return(num*num)
def checkadamnumber(num):
    a= square(num)
    b= square(reversedigit(num))
    if (b==reversedigit(a)):
        return True
    else:
        return False

num=(int(input("enter the value")))
if (checkadamnumber(num)):
    print ("Adam number is True")
else:
    print ("Adam number is False") 


#Armstrong Number
num=(int(input("enter the value")))
k=0
value=num
while value >0:
    a=value%10
    k=k+a**3
    value//=10

if num==k:
    print (num,"is an Armstrong number")
else:
    print (num,"is not an Armstrong number")


#Pallindrome
num=(int(input("enter the value")))
value=num
s=0
while num>0:
    s=(s*10)+num%10
    num//=10
    print (s)

if(value==s):
    print ("value is equal to num")
    print ("s is a Pallindrome")
else:
    print ("s is not a Pallindrome")
    

#Reverse Number
num=(int(input("enter the value")))
num2=num
p=0

while num2>0:
    p=(p*10)+num2%10
    num2//=10

print (p)
print (num)

#Factorial
num=(int(input("enter the value")))
factorial=1
for d in range(1,num+1):
    factorial=factorial*d
    print("The factorial of",num,"is",factorial)

  
