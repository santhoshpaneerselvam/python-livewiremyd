
#Armstrong number

num=153
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
