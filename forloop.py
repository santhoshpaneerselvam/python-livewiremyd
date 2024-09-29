

#simple for
for x in range(8):
	print ("fast this past",x)

#for and break
for x in range(10):
        if x==7:
            break
        print(x)

#for else
for x in range(7):
	print(x)
	if x==4:
	  break
else:
       print ("loop ended")

#for using string
string="good morning"
for x in string:
	print(x)

#collection in for loop 
collection=['welcome',2,'all']
for x in collection:
	print (x)

#neated in for loop
colour=["yellow","sweet","tasty"]
fruits=["mango","papaya","banana"]
for a in colour:
        for b in fruits:
             print (a,b)

#list in for loop 
lists=[["b","o","o","k"],["r","e","a","d"],["w","r","i","t","e"]]
for l in lists:
	print (l)
for x in l:
	print (x)

#continue statement
vegetables=["tomato","potato","cabbage","carrot"]
for x in vegetables:
        if x=="cabbage":
                continue
        print (x)

#increase value
for x in range(5,70,7):
         print (x)



                

