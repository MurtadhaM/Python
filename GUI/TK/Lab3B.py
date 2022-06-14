#!/usr/local/opt/python@3.9/bin/python3.9
"""
Author: Murtadha Marzouq
Assignment: Lab3 Integration Project
"""
import tkinter as tk
import tkinter.font as tkFont
from math import *
# importing the library
from py4j.java_gateway import JavaGateway
# creating a gateway object
gateway = JavaGateway()   
calculate_app = gateway.entry_point
def compute(event):
  calculate_app.setInfo(str(name.get()), float(salary.get()), float(hours.get()))
  # updating the values 
  calculate_app.AddSal()
  calculate_app.AddWork()
  # updating the value
  result.configure(text = "output: " + str(calculate_app.printSal()))
  
large_font = ('Courier',20)
small_font = ('sans-serif',10)
t = tk.Tk()
t.title("Murtadha Marzouq's Lab3")
name = tk.StringVar(value='name') 
salary = tk.StringVar(value='salary')
hours = tk.StringVar(value='hours')
t.geometry("500x300")

tk.Label(t, text="Enter Name:",font=large_font).pack() 
name = tk.Entry(t,textvariable=name,font=large_font,width=100)
name.pack()

tk.Label(t, text="Enter Salary:",font=large_font).pack()
salary= tk.Entry(t,textvariable=salary,font=large_font,width=100)
salary.pack()

tk.Label(t, text="Enter Hours:",font=large_font).pack() 
hours= tk.Entry(t,textvariable=hours,font=large_font,width=100)
hours.pack()

button = tk.Button(t, text="Calculate",font=large_font)
button.bind('<Button-1>', compute)
button.pack()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
result = tk.Label(t, text="", font=fontStyle)
result.pack()
t.mainloop()


