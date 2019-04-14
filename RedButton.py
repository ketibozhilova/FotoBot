#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    self.slogan = Button(frame,
                         text="Take a picture",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)

  def write_slogan(self):
          print( "Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()