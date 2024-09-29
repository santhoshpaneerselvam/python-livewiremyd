'''
num = 1234567
num1=num
d=0

while num1 >0:
    d=(d*10)+num1%10
    num1//=10
    
print(d)
print(num)

num=int(input("enter the value:"))
value=num
p=0

while num>0:
    p=(p*10)+num%10
    num//=10
print (p)

if (value==p):
    print ("value is equal to num")
    print ("p is pallindrome")
else:
    print ("is not pallindrome")
'''
#adam numbers
def reversedigit(num):
    rev=0
    while(num>0):
        rev=rev*10+num%10
        num//=10
    return rev

def square(num):
    return(num*num)
def checkadamnumber(num):
    a=square(num)
    b=square(reversedigit(num))
    if(b==reversedigit(a)):
       return True
    else:
       return False    

num=12
if (checkadamnumber (num)):
    print ("adam number")
else:
    print ("not a adam numbers")
    
