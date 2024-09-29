'''
import random
import time
import turtle

spawn_interval = 0.05
ball_speed = 4
increase_rotation_step = 0.1

window = turtle.Screen()
window.tracer(0)

spinner = turtle.Turtle()
spinner.rotation_speed = 1.5

colour = random.random(), random.random(), random.random()

balls = []
pool_of_balls = []

def spawn_ball(reference):
    if pool_of_balls:
        balls.append(pool_of_balls.pop())
        balls[-1].showturtle()
    else:
        balls.append(turtle.Turtle())
    balls[-1].shape("circle")
    balls[-1].color(colour)
    balls[-1].turtlesize(0.5)
    balls[-1].penup()
    balls[-1].setposition(reference.position())
    balls[-1].setheading(reference.heading())

def increase_anticlockwise_rotation():
    spinner.rotation_speed += increase_rotation_step

def decrease_anticlockwise_rotation():
    spinner.rotation_speed -= increase_rotation_step

window.onkeypress(increase_anticlockwise_rotation, "Left")
window.onkeypress(decrease_anticlockwise_rotation, "Right")
window.listen()

spawn_timer = time.time()
while True:
    spinner.left(spinner.rotation_speed)

    if time.time() - spawn_timer > spawn_interval:
        spawn_ball(spinner)
        spawn_timer = time.time()

    for ball in balls.copy():
        ball.forward(ball_speed)
        if (abs(ball.xcor()) > window.window_width() / 2
            or abs(ball.ycor()) > window.window_height() / 2):
            ball.hideturtle()
            balls.remove(ball)
            pool_of_balls.append(ball)

    print(len(balls), len(pool_of_balls), len(turtle.turtles()))
    window.update()


from turtle import *
from random import randint
  
speed(0)
penup()
goto(-140, 140)
 
for step in range(15):
    write(step, align ='center')
    right(90)
     
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
         
    penup()
    backward(160)
    left(90)
    forward(20)
 
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')
  
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()
  
for turn in range(10):
    player_1.right(36)
 
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')
  
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()
  
for turn in range(72):
    player_2.left(5)
 
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')
  
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()
  
for turn in range(60):
    player_3.right(6)
 
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('yellow')
  
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()
  
for turn in range(30):
    player_4.left(12)
 
for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))



import turtle

pen = turtle.Turtle()

def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 
   
def heart():

    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112)  
    pen.end_fill() 
  
def text():
    
    pen.up() 
    pen.setpos(-73, 95) 
    pen.down() 
    pen.color('yellow')
    pen.write("HELLO FRIENDS",font=("Lucida Handwriting",12,"bold"))


heart()

text()

pen.ht()


import turtle

screen = turtle.Turtle()

cir= ['red','green','blue','yellow','purple']
turtle.pensize(4)
turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(cir[i])
    turtle.forward(200)
    turtle.right(144)
    
turtle.penup()
turtle.setpos(80,-140)
turtle.pendown()
turtle.pencolor("black")

turtle.done()
    
'''

import turtle

Screen=turtle.Screen()
Screen.bgcolor("green")
Screen.setup(width=1357,height=760)
k=turtle.Turtle()
k.hideturtle()
k.penup()
k.backward(500)
k.left(90)
k.forward(200)
k.right(90)
k.pensize(7)
k.pendown()
k.pencolor("white")
k.fillcolor("blue")
k.begin_fill()
k.forward(1000)
k.right(90)
k.forward(500)
k.right(90)
k.forward(1000)
k.right(90)
k.forward(500)
k.end_fill()
k.penup()
k.backward(450)
k.right(90)
k.pendown()
k.circle(200, 180)
k.left(90)
k.forward(150)
k.left(90)
k.fillcolor("orange")
k.begin_fill()
k.forward(150)
k.circle(-40)
k.right(90)
k.forward(80)
k.right(90)
k.forward(150)
k.end_fill()
k.penup()
k.right(90)
k.forward(70)
k.right(90)
k.forward(30)
k.pendown()
k.right(90)
k.forward(30)
k.circle(10)
k.forward(30)
k.penup()
k.right(90)
k.forward(30)
k.right(90)
k.forward(271)
k.right(90)
k.forward(500)
k.right(90)
k.pendown()
k.forward(500)
k.penup()
k.left(90)
k.forward(500)
k.left(90)
k.forward(50)
k.left(90)
k.pendown()
k.circle(-200, 180)
k.right(90)
k.forward(150)
k.right(90)
k.fillcolor("yellow")
k.begin_fill()
k.forward(150)
k.circle(40)
k.left(90)
k.forward(80)
k.left(90)
k.forward(150)
k.end_fill()
k.penup()
k.left(90)
k.forward(70)
k.left(90)
k.forward(30)
k.pendown()
k.left(90)
k.forward(30)
k.circle(-10)
k.forward(30)
k.penup()
k.left(90)
k.forward(30)
k.left(90)
k.forward(270)
k.left(90)
k.forward(500)
k.left(90)
k.forward(350)
k.pendown()
k.left(90)
k.fillcolor("red")
k.begin_fill()
k.circle(100, 180)
k.circle(100, 180)
k.end_fill()
k.penup()
k.goto(0, 200)
k.right(90)
k.pensize(10)
k.pendown()
k.forward(500)

turtle.done()

