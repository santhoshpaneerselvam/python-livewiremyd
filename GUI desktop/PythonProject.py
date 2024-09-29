import tkinter 
from tkinter import *
from tkinter import ttk,font
from PIL import ImageTk,Image

def SportsMaterials(k):
    k=Tk()
    k.geometry("600x600")
    k.title("SPORTS")
    frame=Frame(k,width=1200,height=50,bg="blue")
    frame.pack()
    f=font.Font(weight="Bold",family="Jazz LET",size=25)
    x=Label(frame,text="Sports Items",font=f)
    x.configure(bg="red",fg="yellow")
    x.place(relx=0.45,rely=0.1)
    
    frame=Frame(k,weight=1000,height=700)
    frame.place(anchor="s",relx=0.50,rely=0.9)
    img=ImageTk.PhotoImage(Image.open("sports.jpg"))
    label=Label(frame,Image=img)
    label.pack()
    
    frame=Frame(k,width=500,height=250,bg="lightblue").place(relx=0.30,rely=0.3)
    f=font.Font(k,weight="Bold",height="Jazz LET",size=20)
    l=Label(frame,text="SPORTS ITEMS")

