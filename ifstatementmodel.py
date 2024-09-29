
name=input("enter your name ")
school=input("enter your school")
age= int(input("enter your age"))
marks=int(input("enter your marks"))

if(age>18 and mark>450):
		print ("your eligible for medical seat")
elif(age>18 and mark>350):
		print ("your eligible for engineering seat")
elif(age>18 and mark>250):
		print ("your eligible for arts and science seat")
else:
		print ("not valid")

