
from tkinter import *
import requests
import os

root = Tk()
root.geometry("300x300")
root.title(" installer ")
d=''
import installermain
def Take_input():
    global d
    d = inputtxt.get("1.0", "end-1c")
    n = open('installermain.py','w')
    Display.config(text="installing...")


    n.write(requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/installer.py').text)
    n.close()

    installermain.install()
    os.remove('installermain.py')
    Display.config(bg='green',text="installed")
l = Label(text = "\/ enter directory \/")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 
Display = Button(root, height = 2,
                 width = 20,
                 text ="install",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()


mainloop()
