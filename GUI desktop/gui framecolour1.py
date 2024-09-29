
from tkinter import *
s=Tk()
s.geometry("500x500")

l0=Label(s,text="RESTAURANT BILL")
l0.grid(row=0,column=6)
l1=Label(s,text="IDLY")
l1.grid(row=2,column=1)
l2=Label(s,text="D0SA")
l2.grid(row=3,column=1)
l3=Label(s,text="POORI")
l3.grid(row=4,column=1)
l4=Label(s,text="PONGAL")
l4.grid(row=5,column=1)
l5=Label(s,text="VADAI")
l5.grid(row=6,column=1)
l6=Label(s,text="TEA")
l6.grid(row=7,column=1)
l7=Label(s,text="PRICE")
l7.grid(row=8,column=1)

e1=Entry(s)
e1.grid(row=2,column=2)
e2=Entry(s)
e2.grid(row=3,column=2)
e3=Entry(s)
e3.grid(row=4,column=2)
e4=Entry(s)
e4.grid(row=5,column=2)
e5=Entry(s)
e5.grid(row=6,column=2)
e6=Entry(s)
e6.grid(row=7,column=2)
e7=Entry(s)
e7.grid(row=8,column=2)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=int(e4.get())
    e=int(e5.get())
    f=int(e6.get())

    g=a+b+c+d+e+f
    e7.insert(0,g)

b=Button(s,text="TOTAL AMOUNT",command=lambda:add())
b.grid(row=8,column=3)




