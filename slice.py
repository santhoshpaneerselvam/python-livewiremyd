
#slice

string="HAVE A GOOD DAY"
s1=slice(3)
s2=slice(2,8,3)
s3=slice(-3,-11,-2)

print ("stringslicing")
print (string [s1])
print (string [s2])
print (string [s3])

#simple
b="hello,world"
print (b[2:7])

#start to slice 
b="hello,world"
print (b[:6])

#slice to end 
b="hello,world"
print (b[3:])

b="hi helloo"
print (b[: : 2])

#negative indexing
b="hello world"
print (b[-7:-1])

#reverse string 
a="happy journey"
print (a[: : -3])

name="livewire computer center"[: : -4]
print (name)




