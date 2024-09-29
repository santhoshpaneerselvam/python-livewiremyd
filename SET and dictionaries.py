'''
fruits={"mango","apple","orange","strawberry","papaya","banana","apple"}
print (fruits)

print ('orange'in fruits)
print ('grapes'not in fruits)


a=set('suresh')
b=set('ramesh')

print (a)

print ("letter in a but not in b",b-a,a-b)
print ("both a or b",a|b)
print ("letters in both a and b",a&b)
print ("letter in a or b but not both",a^b)

#set checking
a={x for x in 'computer science' if x in 'ceumn'}
print (a)
'''
#dictionaries
dic={'name':'santhosh','age':17}
print (dic['name'])

dic['guide']=23 #add
print (dic)

print (list(dic))
print (sorted(dic))
print ('guido'in dic)
print ('guide'in dic)

a=dict([('hari',34),('mani',21),('ramana',25)])
print (a)

dict={x:x**4 for x in (5,7,3)}
print (dict)

a=dict(a=23,b=45,c=54)
print(a)

