from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


frame=LabelFrame(root,text="Validation",padx=50,pady=100)#INTERNAL PADDING


#showinfo, showwarning, showerror, askedquestion, askokcancel, askyesno
def popup():
    respone=messagebox.askyesno("UPDATE!","DONE")
    Label(frame,text=respone).pack
    if respone==1:




frame.pack(padx=20,pady=20)#EXTERNAL PADDING
Button(frame,text="Validation",command=popup).pack()




root.mainloop()