import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *
from tkinter import Canvas

# Initialize the main window
root = tk.Tk()
root.title("Kingdom Calculator")
root.geometry("500x700")  # Increased window size

# Color scheme
BG_COLOR = "#2C3E50"  # Dark blue-gray
BUTTON_COLOR = "#3498DB"  # Bright blue
TEXT_COLOR = "#ECF0F1"  # Off-white
ENTRY_BG = "#34495E"  # Slightly lighter blue-gray

root.configure(bg=BG_COLOR)

# Load the logo image
try:
    logo_image = Image.open("Kingdom.png")
    logo = ImageTk.PhotoImage(logo_image)
    root.iconphoto(False, logo)
except Exception as e:
    print(f"Error loading logo: {e}")

# Create styles
style = ttk.Style()
style.theme_use('clam')
style.configure("TEntry",
                fieldbackground=ENTRY_BG,
                foreground=TEXT_COLOR,
                padding=10,
                relief="flat")
style.configure("TButton",
                background=BUTTON_COLOR,
                foreground=TEXT_COLOR,
                padding=10,
                relief="flat")

# Show a frame
def show_frame(frame):
    frame.tkraise()

# Parse equation for graphing
def parse_equation(equation, x):
    equation = equation.replace('^', '**')
    locals_dict = {'x': x, 'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log}
    return eval(equation, globals(), locals_dict)

# Global variable to store the expression
expression = ""

def buttonclick(number):
    global expression
    expression += str(number)
    prince.insert(tk.END, str(number))
    king.insert(tk.END, str(number))

def clear():
    global expression
    expression = ""
    king.delete(0, tk.END)
    prince.delete(0, tk.END)

def add():
    global expression
    expression += "+"
    prince.insert(tk.END, "+")
    king.insert(tk.END, "+")
    king.delete(0, tk.END)

def multi():
    global expression
    expression += "*"
    prince.insert(tk.END, "*")
    king.insert(tk.END, "*")
    king.delete(0, tk.END)

def subtract():
    global expression
    expression += "-"
    prince.insert(tk.END, "-")
    king.insert(tk.END, "-")
    king.delete(0, tk.END)

def division():
    global expression    
    expression += "/"
    prince.insert(tk.END, "/")
    king.insert(tk.END, "/")
    king.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        king.delete(0, tk.END)
        king.insert(0, result)
        expression = result
    except:
        king.delete(0, tk.END)
        king.insert(0, "Error")
        expression = ""

# Calculator page
def create_calculator_page(container):
    calc_page = tk.Frame(container, bg=BG_COLOR)
    calc_page.grid(row=0, column=0, sticky='nsew')

    # Create the rounded entry frames
    prince_frame = tk.Frame(calc_page, bg=ENTRY_BG, bd=0)
    king_frame = tk.Frame(calc_page, bg=ENTRY_BG, bd=0)

    global prince, king
    prince = ttk.Entry(prince_frame, style="TEntry", justify='center', font=('Arial', 16), width=30)
    king = ttk.Entry(king_frame, style="TEntry", justify='center', font=('Arial', 16), width=30)

    prince.pack(padx=4, pady=4)
    king.pack(padx=4, pady=4)

    prince_frame.grid(row=0, column=0, columnspan=4, padx=12, pady=10)
    king_frame.grid(row=1, column=0, columnspan=4, padx=12, pady=20)

    # Define buttons
    buttons = [
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("+", 3, 3),
        ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
        ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("*", 5, 3),
        ("0", 6, 0), (".", 6, 1), ("=", 6, 2), ("/", 6, 3),
        ("Clear", 7, 0, 2)  # Span 2 columns
    ]

    for button in buttons:
        text = button[0]
        row = button[1]
        col = button[2]
        colspan = 1 if len(button) == 3 else button[3]

        if text == "=":
            command = equal
        elif text == "Clear":
            command = clear
        elif text == "+":
            command = add
        elif text == "-":
            command = subtract
        elif text == "*":
            command = multi
        elif text == "/":
            command = division
        else:
            command = lambda x=text: buttonclick(x)
        
        btn = ttk.Button(calc_page, text=text, command=command, style="TButton")
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky='nsew')

    # Configure grid weights
    for i in range(8):
        calc_page.grid_rowconfigure(i, weight=1)
    for i in range(4):
        calc_page.grid_columnconfigure(i, weight=1)

    # Add the "Graph" button at the bottom
    graph_button = ttk.Button(calc_page, text="Switch to Graph", command=lambda: show_frame(graph_page), style="TButton")
    graph_button.grid(row=8, column=0, columnspan=4, sticky='ew', padx=5, pady=5)

    return calc_page

# Graph page
def create_graph_page(container):
    graph_page = tk.Frame(container, bg=BG_COLOR)
    graph_page.grid(row=0, column=0, sticky='nsew')
    
    equation_label = tk.Label(graph_page, text="Enter equation (use 'x' as variable):", bg=BG_COLOR, fg=TEXT_COLOR, font=('Arial', 12))
    equation_label.pack(pady=5)
    
    equation_entry = ttk.Entry(graph_page, style="TEntry", width=40, font=('Arial', 12))
    equation_entry.pack(pady=5)
    
    range_frame = tk.Frame(graph_page, bg=BG_COLOR)
    range_frame.pack(pady=5)
    
    x_min_label = tk.Label(range_frame, text="X min:", bg=BG_COLOR, fg=TEXT_COLOR)
    x_min_label.pack(side=tk.LEFT, padx=5)
    x_min_entry = ttk.Entry(range_frame, style="TEntry", width=10)
    x_min_entry.pack(side=tk.LEFT, padx=5)
    
    x_max_label = tk.Label(range_frame, text="X max:", bg=BG_COLOR, fg=TEXT_COLOR)
    x_max_label.pack(side=tk.LEFT, padx=5)
    x_max_entry = ttk.Entry(range_frame, style="TEntry", width=10)
    x_max_entry.pack(side=tk.LEFT, padx=5)
    
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.tick_params(axis='x', colors=TEXT_COLOR)
    ax.tick_params(axis='y', colors=TEXT_COLOR)
    for spine in ax.spines.values():
        spine.set_color(TEXT_COLOR)
    
    canvas = FigureCanvasTkAgg(fig, master=graph_page)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def plot_graph():
        equation = equation_entry.get()
        x_min = float(x_min_entry.get())
        x_max = float(x_max_entry.get())
        
        x = np.linspace(x_min, x_max, 1000)
        try:
            y = [parse_equation(equation, xi) for xi in x]
            
            ax.clear()
            ax.plot(x, y, color=BUTTON_COLOR)
            ax.set_xlabel('x', color=TEXT_COLOR)
            ax.set_ylabel('y', color=TEXT_COLOR)
            ax.set_title(f'Graph of {equation}', color=TEXT_COLOR)
            ax.grid(True, color=TEXT_COLOR, linestyle='--', linewidth=0.5, alpha=0.5)
            ax.set_facecolor(BG_COLOR)
            
            canvas.draw()
        except Exception as e:
            print(f"Error plotting graph: {e}")
    
    plot_button = ttk.Button(graph_page, text="Plot Graph", command=plot_graph, style="TButton")
    plot_button.pack(pady=10)
    
    back_button = ttk.Button(graph_page, text="Back to Calculator", command=lambda: show_frame(calc_page), style="TButton")
    back_button.pack(side='bottom', fill='x', padx=5, pady=5)
    
    return graph_page

# Create a container frame
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create pages
calc_page = create_calculator_page(container)
graph_page = create_graph_page(container)

# Configure grid
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Show the calculator page first
show_frame(calc_page)

root.mainloop()