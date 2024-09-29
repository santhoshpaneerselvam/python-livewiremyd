
#open("schooldetails.text","x")
#f=open("schooldetails.txt","w")
#f=write("schooldetails")
#f=open("schooldetails.txt","a")
#f=write("\nname\tclass\tschoolname\tplace")
#f=open("schooldetails.txt","r")
#a=f.read()
#print(a)

a=input("enter the name:")
b=int(input("enter the class:"))
c=input("enter the schoolname:")
d=input("enter the place:")
f=open("schooldetails.txt","r")
lines=f.read().split("\n")
for x in lines:
    schooldetails=x.split("\t")
if schooldetails[0]==a and schooldetails[1]==b and schooldetails[2]==c and schooldetails[3]==d:
    print ("schooldetails right")
else:
    print ("schooldetails wrong")





         
