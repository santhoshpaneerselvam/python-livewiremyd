
#reverse number
num=int(input("enter the value"))
num1=num
d=0

while num1 >0:
    d=(d*10)+num1%10
    num1//=10
    
print(d)
print(num)

'''
#pallindrome
num=int(input("enter the value"))
value=num
k=0
while num>0:
    k=(k*10)+num%10
    num//=10
print(k)
if(value==k):
    print ("the value is equal to num")
    print ("k is a pallindrome")
else:
    print ("k is not pallindrome")

#adam number
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


num=int(input("enter the value"))
if (checkadamnumber(num)):
        print ("adam number is true")
else:
    print ("adam number is false")


#armstrong number
num=int(input("enter the value"))
sum=0
num2=num

while (num2 >0):
    value=num2%10
    sum+=value**3
    num2//=10
    print(num)

if num==sum:
    print (num,"is a armstrong number")
else:
    print (num,"is not armstrong number")

'''
    
