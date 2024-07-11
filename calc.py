# Make calculator code
    # Make graphing calc
# Make basic GUI
    # Kingdom Theme
# Put together
# import tkinter as tk
from tkinter import *
import math
root = Tk()
root.title("Kingdom Calculator")

king = Entry(root, width=35, borderwidth=5)
king.grid(row=0, column=0, columnspan=3, padx=12, pady=10)
# king.pack()
# king.insert(0,"Enter your name:") 
def buttonclick(number):
    # king.delete(0,END)
    king.insert(END,number)  
# this deleted everything within the textbox begining to End 

def clear():
    king.delete(0,END)
# we need to save the first number input and use it globally

def add():
    first = king.get()
    # global variable
    # assign a variable fnum to the first input number called first
    #delete number since it will be saved in the placeholder fnum
    global fnum 
    global math
    math = "addition"
    fnum = int(first)
    king.delete(0,END)
    

def multi():
    first = king.get()
    # global variable
    # assign a variable fnum to the first input number called first
    #delete number since it will be saved in the placeholder fnum
    global fnum 
    global math
    math = "multiplication"
    fnum = int(first)
    king.delete(0,END)

def subtract():
    first = king.get()
    # global variable
    # assign a variable fnum to the first input number called first
    #delete number since it will be saved in the placeholder fnum
    global fnum 
    global math
    math = "subtraction"
    fnum = int(first)
    king.delete(0,END)
    #boba = 4
    #if boba == 5
        #print("5 years old")
    #if boba == 4
        #print("4 years old")
def Division():
    first = king.get()
    # global variable
    # assign a variable fnum to the first input number called first
    #delete number since it will be saved in the placeholder fnum
    global fnum 
    global math
    math = "Division"
    fnum = int(first)
    king.delete(0,END)

def equal():
    #same process we need a memory for the second variable
    #delete after puttin in a number
    second = king.get()
    king.delete(0,END)
    #addition to + 
    if math == "addition":
        king.insert(0,fnum + int(second))
    elif math == "division":
        king.insert(0,fnum / int(second))
    elif math == "subtration":
        king.insert(0,fnum - int(second))    
    elif math == "multiplication":
        king.insert(0,fnum * int(second))
    else:
        print("error")
    
       
   

#define buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonclick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonclick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonclick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonclick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonclick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonclick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonclick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonclick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonclick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonclick(0))
buttonEq = Button(root,text="=", padx=40, pady=20, command=lambda: equal())
buttonClear = Button(root,text="Clear", padx=29.5, pady=20, command=lambda: clear())
buttonplus = Button(root,text="+", padx=40, pady=20, command=lambda:add())
buttonminus = Button(root,text="-", padx=40, pady=20, command=lambda: subtract())
buttonmulti = Button(root,text="*", padx=40, pady=20, command=lambda: multi())
buttonDiv = Button(root, text="/", padx=40, pady=20, command=lambda: Division())
#put the buttons on the screen

space = Label(root, text="", width=1)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)

button0.grid(row=4,column=1)
buttonEq.grid(row=4,column=2)
buttonClear.grid(row=4,column=4)
buttonplus.grid(row=3,column=4)
buttonminus.grid(row=2,column=4)
buttonmulti.grid(row=1,column=4)
buttonDiv.grid(row=4, column =0)

space.grid(row=1, column=3,rowspan=4)


# mybutton = Button(root, text="enter number", command=click)
# mybutton.pack()

root.mainloop()

















# calculation = ""

# def add_to_calculation(symbol):
#     global_calculation
#     calculation += str(symbol)
#     text_result.delete(1.0)

# def evaluate_calculation():
#     pass
# def clear_field():
#     pass

# root = tk.Tk()
# root.geometry("300x275")
# text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
# text_result.grid(columnspan = 5)
# root.mainloop()

