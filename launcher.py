from tkinter import *
import os
def ghostty ():
    os.system("ghostty")
def chromium ():
    os.system("chromium")
def nautilus ():
    os.system("nautilus")
def launcher ():
    os.system("python launcher.py ")
root=Tk()
root.title('hyprland')

lab1 =Label(root, text='simple launcher')
lab1.grid(column=0,row=0)
b1 =Button(root, text='ghostty', command=ghostty)
b1.grid(column=0,row=1)
b2 =Button(root, text='chromium', command=chromium)
b2.grid(column=0,row=2)
b3 =Button(root, text='File manager', command=nautilus)
b3.grid(column=0,row=3)
b4 =Button(root, text='another one', command=launcher)
b4.grid(column=0,row=4)
root.mainloop()
