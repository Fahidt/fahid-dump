import tkinter as tk

import sys,os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from gui.order import full_order

output = []

def receipt_print():
    price = 0
    for i in full_order:
        price = price + i[2]

    header = ("--------Receipt-------------")
    output.append((header))
    for i in range((len(full_order))):
        if full_order == []:
            break
        holder = full_order[0]
        full_order.remove(full_order[0])
        c = 1
        for j in full_order:
            if holder == j:
                full_order.remove(j)
                c += 1
            else:
                pass
        body = (f"{c} x {holder[0]} {holder[1]} £{holder[2]*c}")
        space = ("                                            ")
        output.append((body))
        output.append(space)
    bottom = (f"------------------£{price}")
    output.append((bottom))
    
    return output




def display_order():
    display_window = tk.Toplevel()
    canvas = tk.Canvas(display_window, height = 500, width = 500, bg = "White")
    canvas.pack()
    
    receipt_print()
    
    receipt = tk.Label(display_window,  bg = "white", text=f"{output}", wraplength=300)
    receipt.config(font=("Courier", 12))
    receipt.place(relwidth=1, relheight=0.8,x=15, y=20)
    
    close_tab = tk.Button(display_window, text="Go back", fg="black", bg="lightgrey",command=display_window.destroy)
    close_tab.place(relwidth=0.6, relheight=0.1, x=60, y=440)