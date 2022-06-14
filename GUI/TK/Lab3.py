#!/usr/local/opt/python@3.10/bin/python3.10
"""
Author: Murtadha Marzouq
Assignment: Lab3 Integration Project

"""
from tkinter import Button, Frame, Image, Label, PhotoImage, ttk  # Normal Tkinter.* widgets are not themed!
from math import *
import os
import tkinter as tk

'''
This function takes the input from the user and evaluates it.
:return: The output of the evaluated expression.
'''


def execute_file(parameter):
    import subprocess
    currentdir = os.path.dirname(os.path.abspath(__file__))
    file_to_execute = os.path.join(currentdir, "JavaCalculator.jar")
    output = os.popen("java -jar \"" + file_to_execute + "\"  " + parameter).read()
    return output

def compute(event=None):
            parameter = " \"" + input.get() + "\" "
            result.configure(text=str(execute_file(parameter)))
def clear(event=None):
            result.configure(text = " ")
large_font = ('Curved Sans', 20)
small_font = ('Segoe UI',10)
tkObj = tk.Tk()
tkObj.title("🐍 Lab3 --Murtadha Marzouq 🐍")
entry1Var = tk.StringVar(value='8+sqrt(16)+2^3-(5*(3+2))+abs(-8)')
xdimintion = 500
ydimension = 200
tkObj.geometry(f'{xdimintion}x{ydimension}')
tk.Label(tkObj, text="Hit me with them Equations ፷: ",font=large_font).pack()
input = tk.Entry(tkObj,textvariable=entry1Var,font=large_font,width=120 )
input.pack()
button = tk.Button(tkObj, text="Calculate",font=large_font , command=compute)
button.bind('<Button-1>', compute)
button.pack()
result = tk.Label(tkObj, text="")
result.pack()
button_clear = tk.Button(tkObj, text="Clear",font=large_font , command=clear)
button_clear.bind('<Button-1>', clear)
button_clear.pack()
tkObj.geometry("650x450")
tkObj.mainloop()



