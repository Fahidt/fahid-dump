import tkinter as tk

def scan_customer():
    print("Cusomter info recieved")
    #connect to db and get a random cusomter

def customer_tab():
    print("Opened customer window")
    #Scan  = Pick a random from database
    #write a program that connectsto same SQL and uploads loads of cusomter 
    #cancel = close window
    customer_window = tk.Toplevel()
    
    canvas = tk.Canvas(customer_window, height = 300, width = 300, bg = "black")
    canvas.pack()
    
    customer = tk.Button(customer_window, text="Scan code", fg="black", bg="lightgrey", command=scan_customer)
    customer.place(relwidth=0.4, relheight=0.9,x=20, y=15)
    
    close_window = tk.Button(customer_window, text="Go back", fg="black", bg="lightgrey",command=customer_window.destroy)
    close_window.place(relwidth=0.4, relheight=0.9, x=160, y=15)