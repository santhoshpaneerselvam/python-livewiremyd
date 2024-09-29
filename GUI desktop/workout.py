
import tkinter
from tkinter import messagebox
def content():
    messagebox.showwarning("hiii hello","hi helo")
value=tkinter.Tk()
b=tkinter.Button(value,text="Have a Nice Day",command=content,activebackground="red")
frame=tkinter.Frame(value,bg="green",width=400,height=450)
frame.pack()
b.pack()
value.mainloop()


