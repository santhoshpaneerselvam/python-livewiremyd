'''
num = 1234
num1=num
r=0

while num1 >0:
    r=(r*10)+num1%10
    num1//=10
    
print(r)
print(num)

'''
value=6789
value1=value
reverse_num=0
while value1>0:
    a=value1%10
    reverse_num=(reverse_num*10)+a
    value1//=10
print(reverse_num)
print(value)
'''

num=int(input("enter a value:"))
value=num
a=0
while num>0:
    a=(a*10)+num%10
    num//=10
print(a)
if(value==a):
    print("value is equql to num")
    print("a is pallindrome")
else:
    print("is not pallindrome")

'''


    
