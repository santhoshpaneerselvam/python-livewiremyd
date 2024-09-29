
from tkinter import *
from tkinter import Tk

name=Tk()
text=Text(name,height=5,width=40)
text.insert(INSERT,"welcome to all.....")
text.insert(END,"happy life......")

text.pack()

b=Button(name,text="submit")
b.pack()
text.tag_add("here","1.0","1.19")
text.tag_add("start","1.19","1.39")

text.tag_config("here",background="yellow",foreground="blue")
text.tag_config("start",background="orange",foreground="red")

name.mainloop()

