
#open("document.txt","x")
#f=open("document.txt","w")
#f=write("data collection")
#f=open("document.txt","a")
#f=write("\nsystem\tdata variable")
#f=open("document.txt","r")
#a=f.read()
#print (a)

a="system"
b="data variable"
f=open("document.txt","r")
lines=f.read().split("\n")
for x in lines:
    username=x.split("\t")
    if username[0]==a and username[0]==b:
        print ("logged in")
    else:
        print ("not logged")



        
