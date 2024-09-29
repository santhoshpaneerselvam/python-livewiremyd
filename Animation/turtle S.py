
import turtle
def draw_circle(pen):
    # outer circle
    pen.setposition(0,-280)
    pen.pendown()
    pen.begin_fill()
    pen.color("blue")
    pen.pencolor("white")
    pen.circle(300)
    pen.end_fill()
    pen.penup()


def draw_circle2(pen):
    #inner circle
    pen.pensize(3)
    pen.setposition(0,-230)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.circle(250)
    pen.end_fill()
    pen.penup()


def draw_S(pen):
    #drawing 'S'
    pen.setposition(-75,200)
    pen.pendown()
    pen.begin_fill()
    pen.color("red")
    pen.pensize(10)
    pen.pencolor("white")
    pen.forward(241)
    pen.backward(240)
    pen.right(90)
    pen.forward(170)
    pen.left(90)
    pen.forward(240)
    pen.right(90)
    pen.forward(240)
    pen.right(90)
    pen.forward(320)
    pen.left(90)
    pen.backward(60)
    pen.right(90)
    pen.backward(240)
    pen.left(90)
    pen.backward(120)
    pen.right(90)
    pen.forward(230)
    pen.left(90)
    pen.backward(290)
    pen.right(90)
    pen.backward(280)
    pen.left(120)
    pen.forward(65)
    pen.end_fill()
    pen.penup()


def draw_triangle(pen):
    #Triangle is shape 'S' to make it look like 2d
    pen.pensize(10)
    pen.setposition(-155,-70)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.pencolor("yellow")
    pen.right(30)
    pen.forward(140)
    pen.end_fill()


def draw_arrow(pen):
    #arrow
    pen.forward(70)
    pen.left(42)
    pen.backward(140)
    pen.right(83)
    pen.backward(140)



if __name__ == '__main__':
    win = turtle.Screen()
    win.bgcolor('black')

    adventure = turtle.Turtle()
    adventure.speed(10)
    adventure.pensize(10)
    adventure.penup()

    draw_circle(adventure)
    draw_circle2(adventure)
    draw_S(adventure)
    draw_triangle(adventure)
    draw_arrow(adventure)
    adventure.penup()
    
    adventure.pencolor("blue")

    adventure.hideturtle()
    turtle.done()
    
    
    
