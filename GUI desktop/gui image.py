
from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage

root=Tk()
root.geometry("600x500")
img=PhotoImage(Image.open("photo.jpg"))
label=Label(root,image=img)
label.pack()
root.mainloop()


