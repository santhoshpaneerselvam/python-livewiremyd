
#arithmetic operators
x=57
y=8

print (x+y)             #addition
print (x-y)             #subtraction
print (x*y)             #multiplication
print (x/y)             #division
print (x%y)             #modulus
print (x**y)            #exponentisation
print (x//y)            #floor division


#assingnment operators
x=52
print (x)
x+=5	#x=x+5
print (x)
x-=8	#43-8
print (x)
x*=7
print (x)
x/=3
print (x)
x%=4
print (x)
x**=9
print (x)
x//5
print (x)


#comparision operators 
a=76	#initialize the value of a
b=48	#initialize the value of b

print ('a==b', a==b)
print ('a<b', a<b)
print ('a>b', a>b)
print ('a<=b', a<=b)
print ('a>=b', a>=b)
print ('a!==b', a!=b)


#logical operators
a=35

print ('is the statement true?: ', a>52 and a<40)
print ('any one statement is true?: ', a>30 or a<25)
print ('each statement is true then return false and vice versa:', (not(a>47) and a<30))
print ('each statement is true then return false and vice versa:', (not(a>23) or a<40))


#identity operators
a=["write","read"]
b=["write","read"]
c=b

print (b is c)
print (b is not c)
print (a is c)
print (a is not c)
print (a==b)
print (a!=b)


#membership operators
x=["king","queen"]

print ('is the value  present ? ', "king" in x)
print ('is value is not present ? ', "jack" not in x)
print ("queen" not in x)



