
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage

r=Tk()
r.geometry("600x400")
img=PhotoImage(Image.open("photo.jpg"))
label=Label(r,image=img)
label.pack()
r=Tk()
r.geometry("300x400")

l1=Label(r,text="NAME")
l1.grid(row=0,column=1)
l2=Label(r,text="FATHER NAME")
l2.grid(row=1,column=1)
l3=Label(r,text="AGE")
l3.grid(row=2,column=1)
l4=Label(r,text="PASSWORD")
l4.grid(row=3,column=1)
l5=Label(r,text="PHONE NO")
l5.grid(row=4,column=1)


e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)
e4=Entry(r)
e4.grid(row=3,column=2)
e5=Entry(r)
e5.grid(row=4,column=2)

def reg():
    f=open("file.txt","a")
    f.write("\n"+e1.get()+"\t"+e2.get()+"\n"+e3.get()+"\n"+e4.get()+"\n"+e5.get())

b1=Button(r,text="save",command=lambda:reg())
b1.grid(row=0,column=3)


r.mainloop()

