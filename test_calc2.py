import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Kingdom Calculator")

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

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self):
        Page.__init__(self)
        self.expression = ""
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)
        
        self.setup_ui()

    def setup_ui(self):
        self.styling()
        self.entries()
        self.create_buttons()

    def styling(self):
        style = ttk.Style()
        style.configure("Rounded.TEntry",
            fieldbackground="#FFFFFF",
            background="#3E3E3E",
            padding=4,
            relief="flat")

    def create_rounded_entry(self, style_name):
        frame = Frame(self, bg="#3E3E3E", bd=0)
        entry = ttk.Entry(frame, style=style_name, justify='center', font=('Arial', 12), width=35)
        entry.pack(padx=4, pady=4)
        return frame, entry
    
    def entries(self):
        self.prince_frame, self.prince = self.create_rounded_entry("Rounded.TEntry")
        self.king_frame, self.king = self.create_rounded_entry("Rounded.TEntry")
        self.prince_frame.pack(padx=12, pady=10)
        self.king_frame.pack(padx=12, pady=20)
    
    def buttonclick(self, number):
        self.expression += str(number)
        self.prince.insert(END, str(number))
        self.king.insert(END, str(number))

    def clear(self):
        self.expression = ""
        self.king.delete(0, END)
        self.prince.delete(0, END)

    def add(self):
        self.expression += "+"
        self.prince.insert(END, "+")
        self.king.insert(END, "+")
        self.king.delete(0, END)

    def multi(self):
        self.expression += "*"
        self.prince.insert(END, "*")
        self.king.insert(END, "*")
        self.king.delete(0, END)

    def subtract(self):
        self.expression += "-"
        self.prince.insert(END, "-")
        self.king.insert(END, "-")
        self.king.delete(0, END)

    def Division(self):
        self.expression += "/"
        self.prince.insert(END, "/")
        self.king.insert(END, "/")
        self.king.delete(0, END)

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.king.delete(0, END)
            self.king.insert(0, result)
            self.expression = result
        except:
            self.king.delete(0, END)
            self.king.insert(0, "Error")
            self.expression = ""

    def create_buttons(self):
        button_frame = Frame(self)
        button_frame.pack()
        # Gobal all buttons
        buttons = [
            ("1", 0, 0), ("2", 0, 1), ("3", 0, 2), ("+", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("/", 3, 0), ("0", 3, 1), ("=", 3, 2), ("Clear", 3, 3)
        ]

        for (text, row, col) in buttons:
            if text == "=":
                command = self.equal
            elif text == "Clear":
                command = self.clear
            elif text in ["+", "-", "*", "/"]:
                command = lambda x=text: getattr(self, {"+" : "add", "-" : "subtract", "*" : "multi", "/" : "Division"}[x])()
            else:
                command = lambda x=text: self.buttonclick(x)
            
            button = Button(button_frame, text=text, padx=40, pady=20, command=command)
            button.grid(row=row, column=col, padx=5, pady=5)

        space = Label(button_frame, text="", width=3)
        space.grid(row=1, column=4, rowspan=4)

class Page2(Page):
   def __init__(self):
       Page.__init__(self)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self):
       Page.__init__(self)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1()
        p2 = Page2()
        p3 = Page3()

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()



# def __init__(self, *args, **kwargs):
#     tk.Frame.__init__(self, *args, **kwargs)
#     global space
#     p1 = Page1()
#     p2 = Page2()
#     p3 = Page3()

#     container = tk.Frame(self)
#     container.pack(side="top", fill="both", expand=True)

#     p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#     p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#     p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

#     button1.grid(row=2, column=0)
#     button2.grid(row=2, column=1)
#     button3.grid(row=2, column=2)
#     buttonplus.grid(row=2, column=3)  # Add left padding

#     button4.grid(row=3, column=0)
#     button5.grid(row=3, column=1)
#     button6.grid(row=3, column=2)
#     buttonminus.grid(row=3, column=3)  # Add left padding

#     button7.grid(row=4, column=0)
#     button8.grid(row=4, column=1)
#     button9.grid(row=4, column=2)
#     buttonmulti.grid(row=4, column=3)  # Add left padding

#     buttonDiv.grid(row=5, column=0)
#     button0.grid(row=5, column=1)
#     buttonEq.grid(row=5, column=2)
#     buttonClear.grid(row=5, column=3)  # Add left padding
#     space = Label(root, text="", width=3)
#     space.grid(row=1, column=3,rowspan=4)




#     p1.show()

