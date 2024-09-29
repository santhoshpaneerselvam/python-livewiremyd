
#simple for
for x in range(15):
    print ("fast this time",x)

#for and break
for x in range(12):
    if x==9:
        break
    print(x)

#for else
for x in range(10):
    print(x)
    if x==7:
        break
else:
    print("loop ended")

#for using string
string="good evening"
for x in string:
    print(x)

#collection in for loop
collection=['welcome',2,'all']
for x in collection:
    print (x)

#nested in for loop
colour=["yellow","sweet","tasty"]
fruits=["mango","papaya","banana"]
for a in colour:
    for b in fruits:
        print (a,b)

#list in for loop
lists=[["a","b","c","d"],["e","f","g","h"],["i","j","k","l"]]
for l in lists:
    print (l)
for x in l:
    print (x)

#continue statement
colour=["red","yellow","green","blue","white","orange"]
for x in colour:
    if x=="white":
        continue
    print (x)

#increase value
for x in range (2,65,4):
    print (x)


    
