
import tkinter
varie=tkinter.Tk()
varie.mainloop()


from tkinter import *
root=Tk()
root.geometry ("300x300")
frame=Frame(root,bg="red",height=80,width=400)
frame.pack()
root.mainloop()


from tkinter import *
root=Tk()
frame=Frame(root,bg="yellow",height=600,width=800)
frame.pack()
root.mainloop()


import tkinter
from tkinter import messagebox
def content():
    messagebox.showwarning("goood morning","good moning")
value=tkinter.Tk()
b=tkinter.Button(value,text="welcome to python",command=content)
b.pack()
value.mainloop()


import tkinter
t=tkinter.Tk()
frame=tkinter.Frame(t,bg="blue",width=500,height=500)
b=tkinter.Button(t,text="hello",activebackground="orange")
frame.pack()
b.pack()
t.mainloop()

from tkinter import *
root=Tk()
for fm in ['orange','green','yellow','red','lightblue','pink','black','white','violet','darkblue','grey','purple']:
    Frame(height=30,width=650,bg=fm).pack()
root.mainloop()


