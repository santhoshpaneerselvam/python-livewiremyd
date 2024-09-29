
name="santhosh"
place="mayiladuthurai"
age=19

if(age>18 and place=="sembanarkovil"):
    print(name,"is eligible for vote")
else:
    print(name,"is eligible for vote")

#Get User input
year=int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


name="keerthi"
place="trichy"
age=18

if(age>17 and place=="trichy"):
    print(name,"is eligible for vote")
elif(age<18 and place=="trichy"):
    print(name,"not eligible for vote")
elif(age>17):
    print(name,"is eligible")
elif(place=="trichy"):
    print(name,"is eligible for voting")


year=int(input("enter the year:"))
if(year%4==0 and year%100!=0)or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


