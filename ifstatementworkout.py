
name=input("enter the name")
school=input("enter the school")
age=int(input("enter the age"))
tamil=int(input("enter the tamil marks"))
english=int(input("enter the english marks"))          
maths=int(input("enter the maths marks"))
science=int(input("enter the science marks"))
socialscience=int(input("enter the social science"))
marks=int(tamil+english+maths+science+socialscience)

if (age>18 and marks>450):
    print ("your eligible for medical seat")
elif (age>18 and marks>350):
    print ("your eligible for engineering seat")
elif (age>18 and marks>250):
    print ("your eligible for arts and science")
else:
    print ("not eligible")
