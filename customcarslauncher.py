
import os
import tkinter as tk
import tkinter.ttk as ttk
import requests
import updater 
root = tk.Tk()
root.title("Launcher")
root.geometry("400x400")
def startcustomcars():
  i=0
  f=open('version.txt','r')
  if not f.read()==requests.get('https://raw.githubusercontent.com/bestbinaryboi/customcars/main/version.txt').text:
    updater.install()    
    while not updater.done==1:
      i=i
    import customcarsthirdpersoncontroller
    root.destroy()
  else:
    import customcarsthirdpersoncontroller
    root.destroy()
    
    
 
 
b=Button(text="start custom cars",command=startcustomcars())

 
 
root.mainloop()
