import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

s=Tk()
s.geometry("500x400")
frame=Frame(s,width=50,height=50)
frame.pack()
frame.place(anchor="n",relx=0.50,rely=0.0)
img=ImageTk.PhotoImage(Image.open("picture.jfif"))
label=Label(frame,image=img)
label.pack()

l0=Label(s,text="FOOD")
l0.place(relx=0.50,rely=0.0)
l1=Label(s,text="DOSA")
l1.place(relx=0.05,rely=0.2)
l2=Label(s,text="POORI")
l2.place(relx=0.05,rely=0.3)
l3=Label(s,text="CURD RICE")
l3.place(relx=0.05,rely=0.4)
l4=Label(s,text="IDLY")
l4.place(relx=0.05,rely=0.5)
l5=Label(s,text="LEMON RICE")
l5.place(relx=0.05,rely=0.6)
l6=Label(s,text="CHAPPATI")
l6.place(relx=0.05,rely=0.7)
l7=Label(s,text="PRICE")
l7.place(relx=0.05,rely=0.8)

e1=Entry(s)
e1.place(relx=0.2,rely=0.2)
e2=Entry(s)
e2.place(relx=0.2,rely=0.3)
e3=Entry(s)
e3.place(relx=0.2,rely=0.4)
e4=Entry(s)
e4.place(relx=0.2,rely=0.5)
e5=Entry(s)
e5.place(relx=0.2,rely=0.6)
e6=Entry(s)
e6.place(relx=0.2,rely=0.7)
e7=Entry(s)
e7.place(relx=0.2,rely=0.8)

def add():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=int(e4.get())
    e=int(e5.get())
    f=int(e6.get())
    g=a+b+c+d+e+f
    e7.insert(0,g)

b=Button(s,text="ENTER",command=lambda:add())
b.place(relx=0.3,rely=0.8)


s.mainloop()

