
from tkinter import *
r=Tk()
n=IntVar()
c=Checkbutton(r,text="word1").pack()
c1=Checkbutton(r,text="word2").pack()
c2=Checkbutton(r,text="word3").pack()
c3=Checkbutton(r,text="word4").pack()
from PIL import Image
from PIL.ImageTk import PhotoImage

r.geometry("600x500")
img=PhotoImage(Image.open("photo.jpg"))
label=Label(r,image=img)
label.pack()
r.mainloop()


