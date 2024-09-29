
from tkinter import *
k=Tk()
k.geometry("600x600")

l0=Label(k,text="PRODUCT")
l0.grid(row=0,column=6)
l1=Label(k,text="PEN")
l1.grid(row=2,column=1)
l2=Label(k,text="PENCIL")
l2.grid(row=3,column=1)
l3=Label(k,text="SCALE")
l3.grid(row=4,column=1)
l4=Label(k,text="PRICE")
l4.grid(row=5,column=1)

e1=Entry(k)
e1.grid(row=2,column=2)
e2=Entry(k)
e2.grid(row=3,column=2)
e3=Entry(k)
e3.grid(row=4,column=2)
e4=Entry(k)
e4.grid(row=5,column=2)

def multi():
    a=int(e1.get())
    b=int(e2.get())
    c=int(e3.get())
    d=a*b*c
    e4.insert(0,d)
    
b=Button(k,text="ENTER",command=lambda:multi())
b.grid(row=5,column=3)





k.mainloop()
