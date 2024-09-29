
Name=(input("enter the name"))
Age=(int(input("enter the age")))
Fathername=(input("enter the father name"))
Mothername=(input("enter the mother name"))
School=(input("enter the school name"))
Place=(input("enter the Place"))
Tamil=(int(input("enter the tamil mark")))
English=(int(input("enter the english mark")))
Maths=(int(input("enter the maths mark")))
Physics=(int(input("enter the physics mark")))
Chemistry=(int(input("enter the chemistry mark")))
Biology=(int(input("enter the biology mark")))
Marks=(Tamil+English+Maths+Physics+Chemistry+Biology)
print(Marks)

    
if (Age>18 and Marks>500):
    print ("Your Eligible For Medical Seat")
elif (Age>18 and Marks>400):
    print ("Your Eligible For Engineering Seat")
elif (Age>18 and Marks>300):
    print ("Your Eligible For Arts and Science Seat")
else:
    print ("Not Eligible")
    
