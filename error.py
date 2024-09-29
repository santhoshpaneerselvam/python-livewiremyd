
#print(x)

try:
    print(x)
except:
    print("an error occured")

try:
  b=10+a
except NameError:
    print("variable a is not defined")
except:
    print("something elses went wrong")
  
try:

   print(4)
except:
    print("someting went wrong")
else:
    print("nothing went wrong")

try:
    x=5
    print(x)
except:
    print("someting went wrong")
finally:
    print("the 'try except' is finished")

#raise exception("qwertyuiop")
    
a="hello"
#assert a=="bala"
assert a=="hello"
