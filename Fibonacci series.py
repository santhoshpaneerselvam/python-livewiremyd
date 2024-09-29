
#Fibonacci series
def recursive_fibonacci(s):
    if s<=1:
        return s
    else:
        return(recursive_fibonacci(s-1)+recursive_fibonacci(s-2))

s_terms=20

#check if the numbers of terms is valid
if s_terms <=0:
    print ("Invalid input ! Please input a positive value")
else:
    print ("Fibonacci series:")
for k in range (s_terms):
    print (recursive_fibonacci(k))

    
