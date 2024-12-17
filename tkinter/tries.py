import tkinter as tk
from tkinter import ttk

#Make stuff less blurry
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk() #Call root class

# message = tk.Label(root, text= 'Hello World') #Create label
# message.pack() #Make label visible

#Variables of screen
root.title('Demo mode')
title = root.title

root.geometry('600x400+50+50') #widthxheight±x±y
#Window displaying
root.mainloop()