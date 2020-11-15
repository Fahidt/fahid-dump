import tkinter as tk
from tkinter import filedialog, Text
import os
import datetime as dt
from gui.customer import scan_customer, customer_tab
from gui.order import order_tab, full_order, order_upload
from gui.confirm import confirm_tab
from gui.display import display_order, output
from class_.food import Food

def cancel_order():
    full_order.clear()
    order_upload.clear()
    output.clear()

def main_page():
    root = tk.Tk()

    canvas = tk.Canvas(root, height = 700, width = 700, bg = "black")
    canvas.pack()

    frame = tk.Frame(root, bg = "MistyRose1")
    frame.place(relwidth=0.95, relheight=0.95,relx=0.025, rely=0.025)

    our_info = tk.Label(frame,  bg = "white", text="Rice World")
    our_info.config(font=("Courier", 40))
    our_info.place(relwidth=0.5, relheight=0.2,relx=0.25, rely=0.04)

    customer = tk.Button(frame, text="Customer", padx=40, pady=150, fg="black", bg="lightgrey", command=customer_tab)
    customer.place(x=60, y=175)

    order = tk.Button(frame, text="Order", padx=52, pady=150, fg="black", bg="lightgrey", command=order_tab)
    order.place(x=265, y=175)

    confirm = tk.Button(frame, text="Confirm", padx=42, pady=150, fg="black", bg="lightgrey", command=confirm_tab)
    confirm.place(x=470, y=175)
    
    recepit = tk.Button(frame, text="Receipt", padx=50, pady=42, fg="black", bg="lightgrey", command=display_order)
    recepit.place(relwidth=0.715, relheight=0.1,x=100, y=520)
    
    cancel = tk.Button(frame, text="New Order", padx=50, pady=42, fg="black", bg="lightgrey", command=cancel_order)
    cancel.place(relwidth=0.714, relheight=0.1,x=100, y=590)
    
    root.mainloop()

main_page()

# Make a file which adds many people to a database 
# 1 - scan code will pick a random number from customer db 
# 2 - confirm button will =  load that customer into a list with 4 section customer name, rice, meat, cost, data and clear lists 
# 3 - are you sure = upload to rice world database

# 4 - data button in top right which opens up a page with some data  