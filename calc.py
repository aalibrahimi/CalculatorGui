import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Kingdom Calculator")
# root2 = tk.Tk()
# root2.title("Page 2")


# Load the logo image using PIL and convert to a format Tkinter can use
try:
    logo_image = Image.open("Kingdom.png")  # Replace with the correct path to your logo image
    logo = ImageTk.PhotoImage(logo_image)
    root.iconphoto(False, logo)  # Set the logo as the window icon
except Exception as e:
    print(f"Error loading logo: {e}")

# Create a style for the Entry widget
style = ttk.Style()
style.configure("Rounded.TEntry",
                fieldbackground="#FFFFFF",
                background="#3E3E3E",
                padding=4,
                relief="flat")

# Create a rounded corner frame
def create_rounded_entry(parent, style_name):
    frame = Frame(parent, bg="#3E3E3E", bd=0)
    entry = ttk.Entry(frame, style=style_name, justify='center', font=('Arial', 12), width=35)
    entry.pack(padx=4, pady=4)
    return frame, entry

# Create the entries with rounded borders
prince_frame, prince = create_rounded_entry(root, "Rounded.TEntry")
king_frame, king = create_rounded_entry(root, "Rounded.TEntry")

prince_frame.grid(row=0, column=0, columnspan=4, padx=12, pady=10)
king_frame.grid(row=1, column=0, columnspan=4, padx=12, pady=20)

# Global variable to store the expression
expression = ""

def buttonclick(number):
    global expression
    expression += str(number)  # Convert number to string and append to expression
    prince.insert(END, str(number))  # Insert number as string in the prince Entry widget
    king.insert(END, str(number))  # Insert number as string in the king Entry widget
def clear():
    global expression
    expression = ""  # Clear the expression
    king.delete(0, END)
    prince.delete(0, END)

def add():
    global expression
    expression += "+"
    prince.insert(END, "+")
    king.insert(END, "+")
    king.delete(0,END)

def multi():
    global expression
    expression += "*"
    prince.insert(END, "*")
    king.insert(END, "*")
    king.delete(0,END)

def subtract():
    global expression
    expression += "-"
    prince.insert(END, "-")
    king.insert(END, "-")
    king.delete(0,END)

def Division():
    global expression    
    expression += "/"
    prince.insert(END, "/")
    king.insert(END, "/")
    king.delete(0,END)

def equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression and convert result to string
        king.delete(0, END)
        king.insert(0, result)
        expression = result  # Update expression with the result for further calculations
    except:
        king.delete(0, END)
        king.insert(0, "Error")
        expression = ""

# def graph():
#     global root2, root
#     root.lift()
#     root2.mainloop()
#     root2 = tk.Tk()
#     root2.title("Page 2")

# https://stackoverflow.com/questions/48796807/how-to-create-and-display-multiple-widgets-using-a-loop-tkinter --> Idk classes


# # Define buttons
# button1 = Button(root2, text="1", padx=40, pady=20, command=lambda: buttonclick(1))
# button2 = Button(root2, text="2", padx=40, pady=20, command=lambda: buttonclick(2))
# button3 = Button(root2, text="3", padx=40, pady=20, command=lambda: buttonclick(3))
# button4 = Button(root2, text="4", padx=40, pady=20, command=lambda: buttonclick(4))
# button5 = Button(root2, text="5", padx=40, pady=20, command=lambda: buttonclick(5))
# button6 = Button(root2, text="6", padx=40, pady=20, command=lambda: buttonclick(6))
# button7 = Button(root2, text="7", padx=40, pady=20, command=lambda: buttonclick(7))
# button8 = Button(root2, text="8", padx=40, pady=20, command=lambda: buttonclick(8))
# button9 = Button(root2, text="9", padx=40, pady=20, command=lambda: buttonclick(9))
# button0 = Button(root2, text="0", padx=40, pady=20, command=lambda: buttonclick(0))
# buttonEq = Button(root2, text="=", padx=40, pady=20, command=equal)
# buttonClear = Button(root2, text="Clear", padx=29.5, pady=20, command=clear)
# buttonplus = Button(root2, text="+", padx=40, pady=20, command=add)
# buttonminus = Button(root2, text="-", padx=40, pady=20, command=subtract)
# buttonmulti = Button(root2, text="*", padx=40, pady=20, command=multi)
# buttonDiv = Button(root2, text="/", padx=40, pady=20, command=Division)
# buttonGraph = Button(root2, text="Graph", padx=40, pady=20, command=graph)

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
buttonEq = Button(root, text="=", padx=40, pady=20, command=equal)
buttonClear = Button(root, text="Clear", padx=29.5, pady=20, command=clear)
buttonplus = Button(root, text="+", padx=40, pady=20, command=add)
buttonminus = Button(root, text="-", padx=40, pady=20, command=subtract)
buttonmulti = Button(root, text="*", padx=40, pady=20, command=multi)
buttonDiv = Button(root, text="/", padx=40, pady=20, command=Division)
# buttonGraph = Button(root, text="Graph", padx=40, pady=20, command=graph)



# Remove the spacer Label
# buttonplus.grid(row=2, column=3, columnspan=4)
# spacer = Label()
# Modify the button placement
space = Label(root, text="", width=3)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
buttonplus.grid(row=2, column=3)  # Add left padding

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonminus.grid(row=3, column=3)  # Add left padding

button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
buttonmulti.grid(row=4, column=3)  # Add left padding

buttonDiv.grid(row=5, column=0)
button0.grid(row=5, column=1)
buttonEq.grid(row=5, column=2)
buttonClear.grid(row=5, column=3)  # Add left padding
space.grid(row=1, column=3,rowspan=4)

# buttonGraph.grid(row=6, column=1, columnspan=2)

root.mainloop()

# Create 2nd file for 2nd page and call file function after destroying main file widget? And just .mainloop() that file/function?