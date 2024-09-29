'''
from turtle import *
forward(100)
left(120)
forward(100)
left(120)
forward(100)
backward(100)
right(120)
color('blue')
width(3)
penup()
pendown()
home()
pos()
clearscreen()
for steps in range(100):
    for c in ('blue','red','green'):
        color(c)
        forward(steps)
        right(0)
        color('red')
        fillcolor('blue')
        bgcolor('yellow')
        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
            end_fill()

          
import turtle             
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.color("black")
def my_sqrfunc(size):
   for i in range(10):
      my_pen.fd(size)
      my_pen.left(90)
      size = size - 5
my_sqrfunc(146)
my_sqrfunc(126)
my_sqrfunc(106)
my_sqrfunc(86)
my_sqrfunc(66)
my_sqrfunc(46)
my_sqrfunc(26)


import turtle             
my_win = turtle.Screen()
turtle.speed(8)
turtle.color("blue")
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
turtle.exitonclick()


import turtle             
colors = [ "violet","indigo","blue","green","yellow","orange","red"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 7])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)

'''
import turtle             
colors = ["orange","white","green"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for k in range(360):
   my_pen.pencolor(colors[k % 3])
   my_pen.width(k/100 + 1)
   my_pen.forward(k)
   my_pen.left(59)


