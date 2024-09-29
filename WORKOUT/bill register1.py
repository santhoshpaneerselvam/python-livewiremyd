
from tkinter import *
from tkinter import ttk,font

bill=Tk()
bill.geometry("700x700")
frame=Frame(bill,width=670,height=700,bg="RED")
frame.place(relx=0.3,rely=0.01)

frame1=Frame(frame,width=560,height=700,bg="YELLOW")
frame1.place(relx=0.1,rely=0.02)

f=font.Font(weight="bold",family="helvetics",size=30)
l0=Label(bill,text="FEES RECEIPT",font=f,bg="burlywood1")
l0.place(relx=0.44,rely=0.0)
f1=font.Font(weight="bold",family="CALIBRI",size=15)
l1=Label(bill,text="ADMISSION NO:",font=f1,bg="bisque1")
l1.place(relx=0.4,rely=0.1)
l2=Label(bill,text="NAME:",font=f1,bg="bisque1")
l2.place(relx=0.4,rely=0.2)
l3=Label(bill,text="COURSE:",font=f1,bg="bisque1")
l3.place(relx=0.4,rely=0.3)
l4=Label(bill,text="ACTUAL FEES:",font=f1,bg="bisque1")
l4.place(relx=0.4,rely=0.4)
l5=Label(bill,text="OFFER FEES:",font=f1,bg="bisque1")
l5.place(relx=0.4,rely=0.5)
l6=Label(bill,text="DISCOUNT:",font=f1,bg="bisque1")
l6.place(relx=0.4,rely=0.6)
l7=Label(bill,text="NET FEES:",font=f1,bg="bisque1")
l7.place(relx=0.4,rely=0.7)
l8=Label(bill,text="GST:",font=f1,bg="bisque1")
l8.place(relx=0.4,rely=0.8)
l9=Label(bill,text="NET AMOUNT:",font=f1,bg="bisque1")
l9.place(relx=0.4,rely=0.9)

mystr=StringVar()
mystr.set('0')
mystr1=StringVar()
mystr1.set('0')
t=font.Font(weight="bold",family="tome new roman",size=13)
a1=Entry(bill,font=t,bg="#7FFFD4")
a1.place(relx=0.6,rely=0.1)
a2=Entry(bill,font=t,bg="#7FFFD4")
a2.place(relx=0.6,rely=0.2)
a3=Entry(bill,font=t,bg="#7FFFD4")
a3.place(relx=0.6,rely=0.3)
a4=Entry(bill,font=t,bg="#7FFFD4")
a4.place(relx=0.6,rely=0.4)
a5=Entry(bill,textvariable=mystr,state=DISABLED,font=t,bg="#7FFFD4")
a5.place(relx=0.6,rely=0.5)
a6=Entry(bill,font=t,bg="#7FFFD4")
a6.place(relx=0.6,rely=0.6)
a7=Entry(bill,font=t,bg="#7FFFD4")
a7.place(relx=0.6,rely=0.7)
a8=Entry(bill,font=t,bg="#7FFFD4")
a8.place(relx=0.6,rely=0.8)
a9=Entry(bill,font=t,bg="#7FFFD4",textvariable=mystr1,state=DISABLED)
a9.place(relx=0.6,rely=0.9)

def feesreceipt():
    f=open("feesreceipt.text","a")
    f.write("\n"+a1.get()+"\n"+a2.get()+"\n"+a3.get()+"\n"+a4.get()+"\n"+a5.get()+"\n"+a6.get()+"\n"+a7.get()+"\n"+a8.get()+"\n"+a9.get())
    a=int(a4.get())
    b=int(a6.get())
    c=a-(a*(b/100))
    print(c)
    mystr.set(str(c))

b=Button(bill,text="TOTAL",bg="#20B2AA",font=t,command=lambda:feesreceipt())
b.place(relx=0.45,rely=0.95)

def fees():
    d=int(a7.get())
    e=int(a8.get())
    f=d+(d*(e/100))
    print(f)
    mystr1.set(str(f))

b1=Button(bill,text="SAVE",font=t,bg="#20B2AA",command=lambda:fees())
b1.place(relx=0.55,rely=0.96)

bill.mainloop()

    
