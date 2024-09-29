'''
import random
import turtle

def isInScreen(win,turt):

    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    turtleX = turt.xcor()
    turtleY = turt.ycor()

    stillIn = True

    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

def sameposition(Red, Blue):
    if Red.pos() == Blue.pos():
        return False
    else:
        return True

def main():
    win = turtle.Screen()
    Red = turtle.Turtle()
    Red.pencolor("red")
    Red.pensize(5)
    Red.shape('turtle')
    pos = Red.pos()

    Blue = turtle.Turtle()
    Blue.pencolor("blue")
    Blue.pensize(5)
    Blue.shape('turtle')
    Blue.hideturtle()

    Blue.penup()
    Blue.goto(pos[0]+50, pos[1])
    Blue.showturtle()
    Blue.pendown()

    mT = True
    jT = True

    while mT and jT and sameposition(Red, Blue):
        
        coinRed = random.randrange(0, 2)
        angleRed = 90
        if coinRed == 0:
            Red.left(angleRed)
        else:
            Red.right(angleRed)
            
        coinBlue = random.randrange(0, 2)
        angleBlue = 90
        if coinBlue == 0:
            Blue.left(angleBlue)
        else:
            Blue.right(angleBlue)

        Red.forward(50)
        Blue.forward(50)

        mT = isInScreen(win, Blue)
        jT = isInScreen(win, Red)

    Red.pencolor("black")
    Blue.pencolor("black")

    if jT == True and mT == False:
        Red.write("Red Won", True, align="center",
                  font=("arial", 15, "bold"))
     
    elif mT == True and jT == False:
        Blue.write("Blue Won", True, align="center",
                   font=("arial", 15, "bold"))
    else:
        Red.write("Draw", True, align="center", 
                  font=("arial", 15, "bold"))
        Blue.write("Draw", True, align="center", 
                   font=("arial", 15, "bold"))

    win.exitonclick()

main()



import turtle

pen = turtle.Turtle()

def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()

pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

pen.goto(0,75)
eye('black',8)

pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
pen.hideturtle()


import turtle
turtle.title('Sierpinski Tree Animation - PythonTurtle.Academy')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
screen = turtle.Screen()
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def sierpinski_tree(x,y,length,tilt,angle, n):
    if n==0: return
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)
    
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt+angle)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt-angle)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

def animate():
    global angle
    turtle.clear()
    sierpinski_tree(0,-250,1000,90,angle,7)
    screen.update()
    angle = 120 if angle <= 20 else angle-2
    screen.ontimer(animate,50)


angle = 120
animate()
screen.mainloop()


import turtle
import random
import colorsys

screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(1000,1000)
screen.title('Chase the Cycler - Pythonturtle_Academy')
turtle.hideturtle()

n=200
chasers = []
for i in range(n):
    chasers.append(turtle.Turtle())

h=0
for i in range(n):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+= 1/n

    chasers[i].color(c)
    chasers[i].up()
    chasers[i].goto(random.uniform(-500,500), random.uniform(-500,500))
chasers[n-1].goto(0,-300)
chasers[n-1].shape('circle')
chasers[n-1].shapesize(1)

def chase():
    for i in range(n-1):
        angle = chasers[i].towards(chasers[i+1])
        chasers[i].seth(angle)
    chasers[n-1].left(2)
    chasers[n-1].fd(10)
    for i in range(n-1):
        chasers[i].fd(10)
    screen.update()
    screen.ontimer(chase,1000//20)

chase()


import turtle
import math

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Hypotrochoid with Python Turtle - PythonTurtle.Academy")
screen.tracer(0,0)

turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.pensize(2)
t = turtle.Turtle()
t.up()
t.hideturtle()
t.speed(0)
tt = turtle.Turtle()
tt.hideturtle()
tt.speed(0)
first = True

r_big=300
r_small=r_big/2.1
d = r_big/1.6

t3 = turtle.Turtle()
t3.hideturtle()
t3.speed(0)
t3.pensize(2)
t3.up()
t3.seth(0)
t3.goto(0,-r_big)
t3.down()
t3.circle(r_big,steps=200)

tt.up()
tt.pensize(1)
tt.color('blue')
first = True

def draw_circle(x,y,angle):
    global first
    turtle.clear()
    turtle.up()
    turtle.seth(0)
    turtle.goto(x,y-r_small)
    turtle.down()
    turtle.color('black')
    turtle.circle(r_small,steps=200)
    turtle.up()
    turtle.goto(x,y)
    turtle.dot(10,'blue')
    turtle.down()
    turtle.seth(angle)
    turtle.color('purple')
    turtle.fd(d)
    turtle.dot(10,'red')
    tt.goto(turtle.xcor(),turtle.ycor())
    if first:
        tt.down()
        first = False

angle = 0
dist = -r_small*angle*math.pi/180
big_radian = dist/r_big
x = (r_big-r_small)*math.cos(big_radian)
y = (r_big-r_small)*math.sin(big_radian)
draw_circle(x,y,angle+big_radian*180/math.pi)
while True:
    angle -= 6
    dist = -r_small*angle*math.pi/180
    big_radian = dist/r_big
    x = (r_big-r_small)*math.cos(big_radian)
    y = (r_big-r_small)*math.sin(big_radian)
    draw_circle(x,y,angle+big_radian*180/math.pi)
    if angle % 360 == 0 and int(round(big_radian*180/math.pi)) % 360 == 0:
        break
    turtle.update()
    
turtle.clear()
t3.clear()
turtle.update()

'''
import turtle
import colorsys
import math

turtle.setup(1000,1000)
turtle.hideturtle()
turtle.title("Tower of Hanoi - PythonTurtle.Academy")
turtle.speed(0)
turtle.tracer(0,0)

n = 5
peg_height = 300
ring_height_max = 10
ring_width_max = 150
ring_width_min = 20
ring_delta = 15
ring_delta_max = 30
ring_height = 20
animation_step = 10

A = [] 
B = []
C = []

T = [] 

def draw_line(x,y,heading,length,pensize,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.fd(length)
    
def draw_scene():
    turtle.bgcolor('light blue')
    draw_line(-600,-100,0,1200,10,'brown')
    for i in range(-250,251,250):
        draw_line(i,-93,90,peg_height,5,'black')

def initialize():    
    global ring_width_max,ring_width_min,ring_ratio,ring_delta
    for i in range(n):
        A.append(i)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor('red')
        t.fillcolor('light green')
        T.append(t)
    ring_delta = min(135/(n-1),ring_delta_max)
    
def draw_single_ring(r, x, k, extra=0):
    global ring_delta
    
    w = ring_width_max - ring_delta*(r-1)
    T[r].up()
    T[r].goto(x-w/2,-95+ring_height*k + extra)
    T[r].down()
    T[r].seth(0)
    T[r].begin_fill()
    for i in range(2):
        T[r].fd(w)
        T[r].left(90)
        T[r].fd(ring_height)
        T[r].left(90)
    T[r].end_fill()
    
def draw_rings():
    for i in range(len(A)):
        draw_single_ring(A[i],-250,i)
    for i in range(len(B)):
        draw_single_ring(B[i],0,i)
    for i in range(len(C)):
        draw_single_ring(C[i],250,i)
  
def move_ring(PP,QQ):
    if PP == "A":
        x = -250
        P = A
    elif PP == "B":
        x = 0
        P = B
    else:
        x = 250
        P = C

    if QQ =="A":
        x2 = -250
        Q = A
    elif QQ == "B":
        x2 = 0
        Q = B
    else:
        x2 = 250
        Q = C

    for extra in range(1,250-(-95+ring_height*(len(P)-1)),animation_step):
        T[P[len(P)-1]].clear()
        draw_single_ring(P[len(P)-1],x,len(P)-1,extra)
        turtle.update()

    T[P[len(P)-1]].clear()
    draw_single_ring(P[len(P)-1],x,len(P)-1,extra)
    turtle.update()
    tp = x
    if x2 > x:
        step = animation_step
    else:
        step = -animation_step
    for tp in range(x,x2,step):
        T[P[len(P)-1]].clear()       
        draw_single_ring(P[len(P)-1],tp,len(P)-1,extra)
        turtle.update()
    T[P[len(P)-1]].clear()
    draw_single_ring(P[len(P)-1],x2,len(P)-1,extra)
    turtle.update()
    Q.append(P[len(P)-1])
    del P[-1]
    for extra in range(250-(-95+ring_height*(len(Q)-1)),0,-animation_step):
        T[Q[len(Q)-1]].clear()
        draw_single_ring(Q[len(Q)-1],x2,len(Q)-1,extra)
        turtle.update()
    T[Q[len(Q)-1]].clear()
    draw_single_ring(Q[len(Q)-1],x2,len(Q)-1)
    turtle.update()   
    return

def tower_of_hanoi(X,Y,Z,n):
    if n == 1:
        move_ring(X,Z)
        return
    tower_of_hanoi(X,Z,Y,n-1)
    move_ring(X,Z)
    tower_of_hanoi(Y,X,Z,n-1)
    
draw_scene()
turtle.update()
n = int(turtle.numinput('Number of Rings','Please enter number of rings:',5,2,10))
initialize()
draw_rings()
tower_of_hanoi("A","B","C",n)
turtle.update()
         
