
names=["santhosh","hari","mani","ramana"]
names2=["dinesh","kumar","sakthi"]
print (names,names2)
print (type(names))

names.append("vishal")
print (names)

names.extend(names2)
print (names)

names.insert(2,"arjun")
print (names)

names.remove("mani")
print (names)

names.pop()
print (names)

print (names.index("ramana"))
print (names.count("santhosh"))

names.reverse()
print ("reverse_list",names)

names.sort()
print (names)


names3=names.copy()
print ("copied_list",names3)

names3.clear()
print (names3)
print (names)

#example
t=[]
print (any(t))
for x in range(15):
    t.append(x*3)

s=[x**4 for x in range(10)]
print(s)

d=[x**5 for x in range(20)if x%4==0]
print(d)

p=[x+y for x in["king","queen","jack"] for y in["s","t","u"]]
print (p)


