

#print (x)
try:
    print (x)
except:
    print ("an error occured")

try:
    b=10+a
except NameError:
    print ("variable a in not defined")
except:
    print("something went wrong")


try:
    print (w)
except:
    print ("something went wrong")
else:
    print ("nothing went wrong")


try:
    print (x)
except:
    print ("something wrong")
finally:
    print ("the'try except'is finished")


#raise exception
a="hello"
assert a=="world"



