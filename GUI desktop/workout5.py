
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def sel():
    selection="you selected the fruits",str(var.get())
    label.config(text=selection)

r=Tk()
var=IntVar()

R1=Radiobutton(r,text="Apple",variable=var,value=1,command=sel)
R1.pack(anchor=N)

R2=Radiobutton(r,text="Mango",variable=var,value=2,command=sel)
R2.pack(anchor=N)

R3=Radiobutton(r,text="Banana",variable=var,value=3,command=sel)
R3.pack(anchor=N)

R4=Radiobutton(r,text="WaterMelon",variable=var,value=4,command=sel)
R4.pack(anchor=N)

R5=Radiobutton(r,text="PineApple",variable=var,value=5,command=sel)
R5.pack(anchor=N)


label=Label(r)
label.pack()

c=Checkbutton(r,text="Apple").pack()
c1=Checkbutton(r,text="Mango").pack()
c2=Checkbutton(r,text="Banana").pack()
c3=Checkbutton(r,text="Grapes").pack()
c4=Checkbutton(r,text="Water Melon").pack()
c5=Checkbutton(r,text="Pine Apple").pack()

def content():
    messagebox.showwarning("WARNING","NOT A FRUITS")
b=tkinter.Button(r,text="TOMATO",command=content,activebackground="YELLOW")
frame=tkinter.Frame(r,bg="RED",width=200,height=250)
frame.pack()
b.pack()
r.mainloop()
