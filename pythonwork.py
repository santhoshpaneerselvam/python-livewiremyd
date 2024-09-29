
#reverse number
num=int(input("enter the value"))
num1=num
t=0

while num1 >0:
    t=(t*10)+num1%10
    num1//=10
    
print(t)
print(num)

#pallindrome
num=int(input("enter the value"))
value=num
k=0

while num>0:
    k=(k*10)+num%10
    num//=10
    print (k)

if (value==k):
    print ("value is equal to num")
    print ("pallindrome is true")
else:
    print ("pallindrome is false")
  
#string pallindrome
a=str('madam')
a==a[::-1]
print(a)

 #Armstrong number
num=1634
a=0
value=num
while value>0:
    r=value%10
    a=a+r**4
    value//=10

if num==a:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")  


#adam number
def reversedigit (num):
    d=0
    while (num>0):
        d=(d*10)+num%10
        num//=10
        return d
def square (num):
    return (num*num)
def checkadamnumber (num):
    a= square (num)
    b= square (reversedigit(num))
    if (b==reversedigit (a)):
        return True
    else:
        return False
num=31
if (checkadamnumber (num)):
    print ("adam number is true")
else:
    print ("adam number is false")


    

    
