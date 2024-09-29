
liststack=[91,82,73,64,50]
print (liststack)

liststack.append(84)
print(liststack)

liststack.append(47)
print (liststack)

liststack.pop()
print (liststack)

#list queue
from collections import deque

queue=deque(["pencil","pen","eraser","scale","sharpner"])
print (queue)

queue.append("calculator")
print (queue)

queue.popleft()
print (queue)

#del
t=[1,2,3,4,5,6,7,8,9]
print(t)

del t[7]
print (t)

del t[4:8]
print (t)

del t[:]
print (t)

del t[:0]
print (t)


