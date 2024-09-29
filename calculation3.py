

def add(a,b):
    print (a+b)

def sub(a,b):
    print (a-b)

def multi(a,b):
    print (a*b)

def div(a,b):
    print (a/b)

a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))

if (c==20):
    add(a,b)
elif (c==24):
    sub(a,b)
elif (c==22):
    multi(a,b)
elif (c==27):
    div(a,b)
else:
    print("not vaild")



