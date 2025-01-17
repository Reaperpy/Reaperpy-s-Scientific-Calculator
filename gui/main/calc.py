from tkinter import *
import math
import time

root = Tk()
root.title("Reaperpy0's Calculator (GUI Version)")

calc_input = Entry(width=25)

result = 0

def calcClick(number):
  current = calc_input.get()
  calc_input.delete(0, END)
  calc_input.insert(0, str(current) + str(number))

def calcClear():
  calc_input.delete(0, END)

def calcAdd():
  global opers
  opers = "add"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)

def calcEqual():
  try:
    second_num = calc_input.get()
    calc_input.delete(0, END)
    if opers == "add":
      calc_input.insert(0, first_num + float(second_num))
    elif opers == "subtract":
      calc_input.insert(0, first_num - float(second_num))
    elif opers == "multiply":
      calc_input.insert(0, first_num * float(second_num))
    elif opers == "divide":
      calc_input.insert(0, first_num / float(second_num))
    elif opers == "sqrt":
      calc_input.insert(0, math.sqrt(first_num))
    elif opers == "expo":
      calc_input.insert(0, first_num ** float(second_num))
    else:
      calc_input.insert(0, "A fatal error has occurred. Please submit a bug report or pull request on the GitHub repo if you see this message. The app will close in 5 seconds.")
      time.sleep(5)
      quit()
  except ValueError:
    calc_input.insert(0, "Please enter a valid value.")
    time.sleep(5)
    calc_input.delete(0, END)
  except OverflowError:
    calc_input.insert(0, "That number is too large to calculate!")
    time.sleep(5)
    calc_input.delete(0, END)

def calcSubtract():
  global opers
  opers = "subtract"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)

def calcMultiply():
  global opers
  opers = "multiply"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)

def calcDivide():
  global opers
  opers = "divide"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)

def calcSqrt():
  global opers 
  opers = "sqrt"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)

def calcExpo():
  global opers
  opers = "expo"
  first_number = calc_input.get()
  global first_num
  first_num = float(first_number)
  calc_input.delete(0, END)


button_1 = Button(padx=30, pady=20, text="1", command=lambda: calcClick(1))
button_2 = Button(padx=30, pady=20, text="2", command=lambda: calcClick(2))
button_3 = Button(padx=30, pady=20, text="3", command=lambda: calcClick(3))
button_4 = Button(padx=30, pady=20, text="4", command=lambda: calcClick(4))
button_5 = Button(padx=30, pady=20, text="5", command=lambda: calcClick(5))
button_6 = Button(padx=30, pady=20, text="6", command=lambda: calcClick(6))
button_7 = Button(padx=30, pady=20, text="7", command=lambda: calcClick(7))
button_8 = Button(padx=30, pady=20, text="8", command=lambda: calcClick(8))
button_9 = Button(padx=30, pady=20, text="9", command=lambda: calcClick(9))
button_0 = Button(padx=30, pady=20, text="0", command=lambda: calcClick(0))
button_c = Button(padx=30, pady=20, text="C", command=calcClear)
button_equal = Button(padx=100, pady=20, text="=", command=calcEqual)
button_add = Button(padx=30, pady=20, text="+", command=calcAdd)
button_subtract = Button(padx=30, pady=20, text="-", command=calcSubtract)
button_multiply = Button(padx=30, pady=20, text="x", command=calcMultiply)
button_divide = Button(padx=30, pady=20, text="/", command=calcDivide)
button_sqrt = Button(padx=30, pady=20, text="√", command=calcSqrt)
button_expo = Button(padx=30, pady=20, text="^", command=calcExpo)
button_decim = Button(padx=30, pady=20, text=".", command=lambda: calcClick("."))

calc_input.grid(row=0, column=0, columnspan=40)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_c.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_equal.grid(row=7, column=0, columnspan=3)
button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)
button_sqrt.grid(row=6, column=0)
button_expo.grid(row=6, column=1)
button_decim.grid(row=6, column=2)

root.mainloop()