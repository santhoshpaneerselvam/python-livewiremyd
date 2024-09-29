'''
import turtle
t=turtle.Turtle()
t.speed(3)
t.pensize(5)
t.color("red")
t.fillcolor("blue")
for x in range(30):
    for x in range(7):
        t.forward(80)

        t.right(40)
        t.backward(50)
        t.left(60)

turtle.done()


import turtle
k=turtle.Turtle()
k.speed(4)
k.pensize(2)
k.pencolor("blue")

for x in range(50):
    for x in range(1):
        k.forward(100)
        k.right(90)
    k.right(20)
    
turtle.done() 


import turtle
s=turtle.Turtle()
s.speed(1)
s.pencolor("green")
s.forward(100)
s.backward(50)
s.right(90)
s.dot()
s.forward(100)
s.home()
s.goto(50,50)
s.shape("triangle")
s.left(750)
s.right(75)
s.forward(70)
s.right(70)
s.forward(110)
turtle.done()


import turtle
r=turtle.Turtle()
r.penup()
r.setpos(-10,30)
r.pendown()
r.pensize(10)
r.pencolor("blue")
r.shape("circle")
r.forward(150)
r.backward(150)
r.right(80)
r.forward(150)
r.left(70)
r.forward(150)
r.left(70)
r.backward(150)
r.left(75)
r.forward(150)
turtle.done()


import turtle
colors=["orange","green","yellow","red","blue","pink","violet"]
sketch=turtle.Pen()
turtle.bgcolor("black")
for i in range(150):
    sketch.pencolor(colors[i % 7])
    sketch.width(i/100 + 1)
    sketch.forward(i)
    sketch.left(70)
turtle.done()


import turtle
m=turtle.Turtle()
color=["orange","white","green"]
turtle.setup(800,800)
m.speed(0.5)
m.width(3)
turtle.bgcolor("black")
for k in range(15):
    for l in range(20):
        m.color([l/20,k/30,1])
        m.right(90)
        m.circle(200-k*5,90)
        m.left(90)
        m.circle(200-k*5,90)
        m.right(180)
        m.circle(60,34)
turtle.done()

'''
import turtle
k=turtle.Turtle()
k.penup()
k.setpos(-20,50)
k.pendown()
k.pensize(7)
k.pencolor("blue")
k.shape("triangle")
k.forward(120)
k.backward(120)
k.right(90)
k.forward(120)
k.left(100)
k.forward(110)
k.right(90)
k.forward(120)
k.right(80)
k.forward(120)
turtle.done()

