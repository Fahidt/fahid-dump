import os
import csv
import datetime as dt
from class_.food import food

class customer:
    def __init__(self, id, date, email):
        self.id = cid
        self.date = date
        self.email = email
    
    def customer_info(self):
        return(self.id,  self.date, self.email)
    
    def __repr__(self):
        return f"id: {self.id}, date: {self.date}, email: {self.email}"

# class food:
#     def __init__(self, rice, meat, cost):
#         self.rice = rice
#         self.meat = meat
#         self.cost = cost
    
#     def  food_info(self):
#         return(self.rice, self.meat, self.cost)
    
#     def __repr__(self):
#         return f"Rice type: {self.rice}, Meat: {self.meat}, Cost: {self.cost}"

def main_menu():
    print("Please select an option from the following:")
    print("    [1] Customer") #add to db
    print("    [2] Order")# add to db
    print("    [3] Complete Order")
    print("    [4] Cancel Order")
    print("    [5] Exit")

def sign_up_menu():
    print("Please select an option from the following:")
    print("    [1] Scan Code") #add to db
    print("    [2] return to previous menu")# add to db

bar = food()

def poo():
    a = 'poo'
    b = 'shit'
    c = 3
    bar = food(a,b,c)
    print(bar)

poo()

# while(True):
#     main_menu()
#     Click = input("Choose number")
#     if int(Click) == 1:
#         sign_up_menu()
#         Click = input("Choose number")
#         if int(Click) == 1:
#             scan_code()
#         else:
#             break
#     elif int(Click) == 2:
#         #Choose type
#         #Choose meat
#         #choose veg
#         #Add item to order
#     elif int(Click) == 3:
#         #
#     elif int(Click) == 4:
#     elif int(Click) == 5:
#         break
#     else: