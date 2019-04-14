#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("270x90")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
