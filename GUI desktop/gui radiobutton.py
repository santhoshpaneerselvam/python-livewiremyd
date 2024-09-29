
from tkinter import *

def sel():
    selection="you selected the fruits",str(var.get())
    label.config(text=selection)

root=Tk()
var=IntVar()

R1=Radiobutton(root,text="Apple",variable=var,value=1,command=sel)
R1.pack(anchor=N)

R2=Radiobutton(root,text="Mango",variable=var,value=2,command=sel)
R2.pack(anchor=N)

R3=Radiobutton(root,text="banana",variable=var,value=3,command=sel)
R3.pack(anchor=N)


label=Label(root)
label.pack()
root.mainloop()

