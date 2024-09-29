
#lambda function
def x(a):
    return a+7
print (x(87))

x=lambda a:a+54
print (x(123))

x=lambda a,b,c,d:a*b*c*d
print (x(6,8,5,2))

def my_func (t):
    return lambda a:a*t
s=my_func(65)
print (s(4))
print (s(7))


#mapping and filtering
data=[4,9,7,6,5]
result1=map(lambda x:x*6,data)
print (list(result1))

result2=filter(lambda x:x%8==0,data)
print (list(result2))

x=lambda a:a*6
print (x(4))

value=[5,7,6,4,3]
result=filter(lambda x:x%9==3,value)
print (list(result))

def a(x):
    return x*7
print (a(54))

x=lambda z:z*5
print (x(34))
