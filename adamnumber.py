
#adam number
def reversedigit(num):
    s=0
    while (num> 0):
        s=(s*10)+num%10
        num//=10
        return s

def square(num):
    return(num*num)
def checkadamnumber(num):
    a= square(num)
    b= square(reversedigit(num))
    if (b==reversedigit(a)):
        return True
    else:
        return False

num=31
if (checkadamnumber(num)):
    print ("adam number")
else:
    print ("not a adam number")


