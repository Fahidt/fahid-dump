import tkinter as tk
import sys,os
from datetime import date
import random

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from gui.order import order_upload
from db_handling.connect import connect


name = ["Musti", "Tango", "Sherif", "Hamma", "Isse", "Abdul", "Hanif", "Gure", "Fahid",  "Abdul", "Hanif", "Abdul", "Hanif", "Abdul", "Hanif", "Abdul", "Hanif", "Abdul", "Hanif", "Abdul", "Hanif" ]
i = (name[(random.randint(0, len(name) - 1))])

def confirm_order():
    connection = connect()
    n = (name[(random.randint(0, len(name) - 1))])
    for i in order_upload:
        r = i[0]
        m = i[1]
        c = i[2]
        d = date.today()
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO rice_t(name_, rice, meat, cost, date_) VALUES (%s,%s,%s,%s,%s)", (n, r,m, c, d ) )
        connection.commit()
        cursor.close()
    connection.close()
    print("order confirmed")
    #send to db

def confirm_tab():
    print("Confirm button pressed")
    #send to database
    #display recepit in new tab
    #close
    confrim_window = tk.Toplevel()
    
    canvas = tk.Canvas(confrim_window, height = 300, width = 300, bg = "black")
    canvas.pack()
    
    confirm = tk.Button(confrim_window, text="Are you sure", fg="black", bg="lightgrey", command=confirm_order)
    confirm.place(relwidth=0.9, relheight=0.4,x=15, y=20)
    
    close_window = tk.Button(confrim_window, text="Go back", fg="black", bg="lightgrey",command=confrim_window.destroy)
    close_window.place(relwidth=0.9, relheight=0.4, x=15, y=160)