import tkinter as tk
from tkinter import Tk,Text
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

#Text boxes
text = Text(root, height=8)
text.pack()
text.insert('1.0', 'This is a Text demo')
text['state'] = 'disabled'


#Key presses
# def backspace_pressed(event):
#     print("BackSpace key pressed.")
#
# button = ttk.Button(root,text='Save')
# button.bind('<BackSpace>', backspace_pressed)
#
# button.focus()
# button.pack(expand = True)
#Window displaying
root.mainloop()