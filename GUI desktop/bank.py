
import tkinter
from tkinter import *
from tkinter import ttk,font
from PIL import ImageTk,Image


def customerlog(k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("BANK")
    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="STATE BANK",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.45,rely=0.1)
    
    frame=Frame(k,width=1000,height=700)
    frame.place(anchor="s",relx=0.50,rely=0.9)
    img=ImageTk.PhotoImage(Image.open("social.jpg"))
    label=Label(frame,image=img)
    label.pack()

    frame=Frame(k,width=500,height=250,bg="pink").place(relx=0.35,rely=0.3)
    f=font.Font(k,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="CUSTOMER LOGIN",font=f,bg="pink").place(relx=0.43,rely=0.3)
    
    p=font.Font(k,weight="bold",family="Times New Roman",size=15)
    l=Label(frame,text="CUSTOMER ID:",font=p,bg="pink").place(relx=0.41,rely=0.4)
    l=Label(frame,text="PASSWORD:",font=p,bg="pink").place(relx=0.41,rely=0.5)

    l1=Entry(frame)
    l1.place(relx=0.54,rely=0.41)
    l2=Entry(frame)
    l2.place(relx=0.54,rely=0.51)
    b=Button(frame,text="LOGIN",font=p,bg="orange")
    b.place(relx=0.50,rely=0.58)

    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    f=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STATE BANK OF INDIA",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.38,rely=0.1)
    k.mainloop()


def file(a,b,c,d,k):
    t=a+" "+b+" "+c+" "+d+" "+"\n"
    f=open("bank.text","a")
    f.write(t)

def customer_reg(k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("BANK")
    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="STATE BANK",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.45,rely=0.1)
    
    frame=Frame(k,width=1000,height=700)
    frame.place(anchor="s",relx=0.50,rely=0.9)
    img=ImageTk.PhotoImage(Image.open("social.jpg"))
    label=Label(frame,image=img)
    label.pack()

    frame=Frame(k,width=500,height=590,bg="light green").place(relx=0.33,rely=0.1)
    f=font.Font(k,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="light green").place(relx=0.40,rely=0.12)

    j=font.Font(k,weight="bold",family="Times New Roman",size=17)
    l=Label(frame,text="NAME:",font=j,bg="light green").place(relx=0.38,rely=0.24)
    l=Label(frame,text="AGE:",font=j,bg="light green").place(relx=0.38,rely=0.32)
    l=Label(frame,text="FATHER NAME:",font=j,bg="light green").place(relx=0.38,rely=0.40)
    l=Label(frame,text="MOTHER NAME:",font=j,bg="light green").place(relx=0.38,rely=0.48)
    l=Label(frame,text="AaDHAR NO:",font=j,bg="light green").place(relx=0.38,rely=0.56)
    l=Label(frame,text="PANCARD NO:",font=j,bg="light green").place(relx=0.38,rely=0.64)
    l=Label(frame,text="PHONE NO:",font=j,bg="light green").place(relx=0.38,rely=0.72)

    l1=Entry(frame)

    l1.place(relx=0.54,rely=0.25)
    l2=Entry(frame)
    l2.place(relx=0.54,rely=0.33)
    l3=Entry(frame)
    l3.place(relx=0.54,rely=0.41)
    l4=Entry(frame)
    l4.place(relx=0.54,rely=0.49)
    l5=Entry(frame)
    l5.place(relx=0.54,rely=0.57)
    l6=Entry(frame)
    l6.place(relx=0.54,rely=0.65)
    l7=Entry(frame)
    l7.place(relx=0.54,rely=0.73)

    b=Button(frame,text="REGISTER",font=j,bg="light blue",command=lambda:file(l1.get(),l2.get(),l3.get(),l4.get(),l5.get(),l6.get(),l7.get(),k))
    b.place(relx=0.47,rely=0.82)

    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    f=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STATE BANK OF INDIA",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.38,rely=0.1)
    k.mainloop()

def adminpage(k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("BANK")
    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="STATE BANK",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.45,rely=0.1)

    frame=Frame(k,width=500,height=590,bg="#4FD6F7").place(relx=0.01,rely=0.1)
    f=font.Font(k,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="CUSTOMER REGISTER",font=f,bg="#4FD6F7").place(relx=0.07,rely=0.12)

    d=font.Font(weight="bold",family="Times New Roman",size=17)
    l=Label(frame,text="NAME:",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.23)
    l=Label(frame,text="AaDHAR NO;",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.32)
    l=Label(frame,text="PANCARD NO:",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.43)
    l=Label(frame,text="PHONE NO:",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.54)
    l=Label(frame,text="MAIL ID:",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.65)
    l=Label(frame,text="ADDRESS:",font=d,bg="#4FD6F7").place(relx=0.05,rely=0.75)

    b=Button(frame,text="Register",font=d,bg="#de9e4b").place(relx=0.14,rely=0.85)

    l1=Entry(frame)
    l1.place(relx=0.17,rely=0.24)
    l2=Entry(frame)
    l2.place(relx=0.17,rely=0.33)
    l3=Entry(frame)
    l3.place(relx=0.17,rely=0.44)
    l4=Entry(frame)
    l4.place(relx=0.17,rely=0.55)
    l5=Entry(frame)
    l5.place(relx=0.17,rely=0.66)
    l6=Entry(frame)
    l6.place(relx=0.17,rely=0.76)

    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    f=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STATE BANK OF INDIA",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.38,rely=0.1)
    k.mainloop()

def admin(a,b,k):
    if(a=="admin" and b=="admin"):
        adminpage(k)
    else:
        adminlog(k)

def adminlog (k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("BANK")
    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="STATE BANK",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.45,rely=0.1)
    
    frame=Frame(k,width=1000,height=700)
    frame.place(anchor="s",relx=0.50,rely=0.9)
    img=ImageTk.PhotoImage(Image.open("social.jpg"))
    label=Label(frame,image=img)
    label.pack()

    frame=Frame(k,width=500,height=250,bg="orange").place(relx=0.33,rely=0.3)
    f=font.Font(k,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="ADMIN LOGIN",font=f,bg="orange").place(relx=0.45,rely=0.3)
    
    s=font.Font(k,weight="bold",family="times new roman",size=15)
    l=Label(frame,text="ADMIN ID:",font=s,bg="orange").place(relx=0.40,rely=0.4)
    l=Label(frame,text="PASSWORD:",font=s,bg="orange").place(relx=0.40,rely=0.5)

    l1=Entry(frame)
    l1.place(relx=0.51,rely=0.41)
    l2=Entry(frame)
    l2.place(relx=0.51,rely=0.51)
    b=Button(frame,text="LOGIN",font=s,bg="pink",command=lambda:admin(l1.get(),l2.get(),k))
    b.place(relx=0.48,rely=0.58)

    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    f=font.Font(k,weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STATE BANK OF INDIA",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.38,rely=0.1)
    k.mainloop()


def Home():
    #Home page
    k=Tk() 
    k.geometry("1000x700")
    k.title("BANK")
    frame=Frame(k,width=1500,height=50,bg="yellow")
    frame.pack()
    f=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="STATE BANK",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.45,rely=0.1)

    frame=Frame(k,width=1000,height=700)
    frame.place(anchor="s",relx=0.50,rely=0.9)
    img=ImageTk.PhotoImage(Image.open("bank.jpg"))
    label=Label(frame,image=img)
    label.pack()

    f=font.Font(weight="bold",family="Times New Roman",size=20)
    b=Button(k,text="Customer Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customerlog(k)).place(relx=0.10,rely=0.5)
    c=Button(k,text="Customer Register",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:customer_reg(k)).place(relx=0.40,rely=0.5)
    d=Button(k,text="Admin Login",font=f,bg="skyblue",activebackground="#FC92C4",command=lambda:adminlog(k)).place(relx=0.71,rely=0.5)
    
    frame=Frame(k,width=1500,height=50,bg="yellow") 
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    f=font.Font(k,weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="STATE BANK OF INDIA",font=f)
    x.configure(bg="yellow",fg="black")
    x.place(relx=0.38,rely=0.1)
    k.mainloop()



Home()
    

    

