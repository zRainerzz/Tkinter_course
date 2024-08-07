from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title("github.com/zRainerzz")

""" Windows icon (replace with your .ico file) """
# root.iconbitmap("tkinter_icon.ico")  # Uncomment for Windows

""" Linux icon (replace with your .png file) """
icon_image = ImageTk.PhotoImage(Image.open("tkinter_icon.png"))
root.iconphoto(True, icon_image)

#designating how big the original window is
root.geometry("600x40")
root.configure(background="green")

#Weather app, api from AirNow.gov



#Creating a request, it has my API Key , you can create a new account or just use my account, since AirNow.gov works only in USA i don't need that api.
try:
    api_req=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=9BE25E99-5FC4-4F57-B4AD-72DC0518FE67")
    api=json.loads(api_req.content)
    city= api[0]["ReportingArea"]
    quality=api[0]['AQI']
    category=api[0]["Category"]["Name"]
except Exception as e:
    api='ERROR...'

mylab=Label(root,pady=5,text=city + "Air Quality: "+ str(quality)+ " "+ category,font=("Helvetica",20),background='green')


mylab.pack()

root.mainloop()