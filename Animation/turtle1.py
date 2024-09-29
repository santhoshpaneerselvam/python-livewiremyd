
import turtle
k=turtle.Turtle()

def curve():
    for t in range(200):
        k.right(1)
        k.forward(1)

def heart():
    k.fillcolor("blue")
    k.begin_fill()
    k.left(140)
    k.forward(173)
    k.pencolor('red')
    k.shape('circle')
    k.pensize(2)
    k.speed(2)
    curve()
    k.left(120)
    curve()
    k.forward(172)
    k.end_fill()

def text():
    k.up()
    k.setpos(-122,130)
    k.down()
    k.color('yellow')
    k.write("<>SANTHOSH<>",font=("Lucida Handwriting",12,"bold"))


heart()
text()
k.ht()


    
    


