
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image


root=Tk()
root.geometry("500x400")
frame=Frame(root,width=50,height=50)
frame.pack()
frame.place(anchor="n",relx=0.5,rely=0.0)
img=ImageTk.PhotoImage(Image.open("photo.jpg"))
label=Label(frame,image=img)
label.pack()

c1=Entry(root)
c1.place(relx=0.2,rely=0.6)
a=Label(root,text="FIRST NAME:")
a.place(relx=0.05,rely=0.5)
b=Label(root,text="SUR NAME:")
b.place(relx=0.05,rely=0.6)
c=Label(root,text="EMAIL-ID:")
c.place(relx=0.05,rely=0.7)
d=Label(root,text="CONTACT NO:")
d.place(relx=0.05,rely=0.8)

a1=Entry(root)
a1.place(relx=0.2,rely=0.5)
b1=Entry(root)
b1.place(relx=0.2,rely=0.7)
d1=Entry(root)
d1.place(relx=0.2,rely=0.8)

R=Label(root,text="GENDER:")
R.place(relx=0.5,rely=0.5)
var=IntVar

R1=Radiobutton(root,text="Male",variable=var,value=1)
R1.place(relx=0.6,rely=0.5)
R2=Radiobutton(root,text="Female:",variable=var,value=2)
R2.place(relx=0.7,rely=0.5)

combol=Label(root,text="PLACE:")
combol.place(relx=0.5,rely=0.6)
combo=ttk.Combobox(root,values=["Chennai","Coimbatore","Trichy","Vellore","Salem","Theni","Erode"])
combo.place(relx=0.6,rely=0.6)
text1=Label(root,text="Message:")
text1.place(relx=0.5,rely=0.7)
text2=Text(root,height=2,width=18)
text2.place(relx=0.6,rely=0.7)


def Santhosh(name):
    messagebox.showwarning("work done",name)

B1=Button(root,text="done",command=lambda:Santhosh(a1.get()))
B1.place(relx=0.7,rely=0.9)

root.mainloop()

