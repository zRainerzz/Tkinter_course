from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")


frame=LabelFrame(root,text="eyes on the button not me, stalker!",padx=50,pady=100)#INTERNAL PADDING


""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("500x500")

def show():
    mylab=Label(root,text=var.get()).pack()

var=StringVar()

c=Checkbutton(root, text="Check Me!",variable=var,onvalue="ON",offvalue="OFF")
#as a bug, you will find the checkbox selected (that's a glitch)
c.deselect()
c.pack()


mybut=Button(root,text="Show Checking",command=show).pack()



root.mainloop()