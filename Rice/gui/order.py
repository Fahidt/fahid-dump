import tkinter as tk

import sys,os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from class_.food import Food

a = Food(None, None, 0)
full_order = []
order_upload = []

def choose_biryani():
    print("choice b")
    a.rice = 'Biryani'
    return a.rice

def choose_paella():
    print("choice p")
    a.rice = 'Paella'
    return a.rice

def choose_rissotto():
    print("choice r")
    a.rice = 'Rissotto'
    return a.rice


def choose_beef():
    print("choice beef")
    a.meat = 'Beef'
    return a.meat

def choose_chicken():
    print("choice chicken")
    a.meat = 'Chicken'
    return a.meat

def choose_prawn():
    print("choice prawn")
    a.meat = 'Prawn'
    return a.meat


def add_item_():
    #have to reset all factors
    a.cost = 0
    if a.rice == 'Biryani':
        a.cost += 3
    elif a.rice == 'Paella':
        a.cost = 3
    elif a.rice == 'Rissotto':
        a.cost += 4
    else:
        pass

    if a.meat == 'Beef':
        a.cost += 3
    elif a.meat == 'Prawn':
        a.cost += 3
    elif a.meat == 'Chicken':
        a.cost += 2
    else:
        pass
    
    r = a.rice
    m = a.meat
    c = a.cost
    
    item_ = [r, m, c]
    print(a)
    print(item_)
    full_order.append(item_)
    order_upload.append(item_)
    print(full_order)
    print(order_upload)
    



def order_tab():
    #Scan  = Pick a random from database
    #write a program that connectsto same SQL and uploads loads of cusomter 
    #cancel = close window
    order_window = tk.Toplevel()
    
    canvas = tk.Canvas(order_window, height = 300, width = 300, bg = "black")
    canvas.pack()
    
    paella = tk.Button(order_window, text="Paella", fg="black", bg="lightgrey", command=choose_paella)
    paella.place(relwidth=0.3, relheight=0.2,x=7.5, y=30)
    
    biryani = tk.Button(order_window, text="Biryani", fg="black", bg="lightgrey", command=choose_biryani)
    biryani.place(relwidth=0.3, relheight=0.2,x=105, y=30)
    
    rissotto = tk.Button(order_window, text="Rissotto", fg="black", bg="lightgrey", command=choose_rissotto)
    rissotto.place(relwidth=0.3, relheight=0.2,x=202.5, y=30)
    
    beef = tk.Button(order_window, text="Beef", fg="black", bg="lightgrey", command=choose_beef)
    beef.place(relwidth=0.3, relheight=0.2,x=7.5, y=120)
    
    chicken = tk.Button(order_window, text="Chicken", fg="black", bg="lightgrey", command=choose_chicken)
    chicken.place(relwidth=0.3, relheight=0.2,x=105, y=120)
    
    prawn = tk.Button(order_window, text="Prawn", fg="black", bg="lightgrey", command=choose_prawn)
    prawn.place(relwidth=0.3, relheight=0.2,x=202.5, y=120)
    
    add_item = tk.Button(order_window, text="Add item", fg="black", bg="lightgrey",command=add_item_)
    add_item.place(relwidth=0.6, relheight=0.1, x=60, y=210)
    
    close_tab = tk.Button(order_window, text="Go back", fg="black", bg="lightgrey",command=order_window.destroy)
    close_tab.place(relwidth=0.6, relheight=0.1, x=60, y=250)
    #New window 
    #Pick rice type (3 images)
    #Pick meat type (beef, chicken. prawn)
    #delete veg from class
    #add item buttom to add to order list