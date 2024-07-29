from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)


top=Toplevel()
top.title("BINGO! the new window")
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
top.iconphoto(True, icon_image)


""" Load and resize image """
img = Image.open("image2.jpg")  # Replace with your image path
img_resized = img.resize((400, 400))
photo = ImageTk.PhotoImage(img_resized)



""" Display image on label """
my_label = Label(top,image=photo)
my_label.pack()



root.mainloop()