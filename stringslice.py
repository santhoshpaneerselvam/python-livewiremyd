#slice

string="DIAMONDS ARE FOREVER"
s1=slice(8)
s2=slice(3,11,4)
s3=slice(-4,-9,-2)

print ("stringslicing")
print (string[s1])
print (string[s2])
print (string[s3])

#simple
b="good, morning"
print (b[3:8])

#start to slice 
b="good, morning"
print (b[:4])

#slice to end 
b="good, morning"
print (b[2:])

b="good morning"
print (b[: : 5])

#negative indexing 
b="good evening"
print (b[-8 : -2])

#reverse string 
a="good night"
print (a[: : -3])

name="livewire computer center"[: : -4]
print (name) 




