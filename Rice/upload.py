from db_handling.connect import connect
import random

name = ["Andrei","Rebekah","Jacob","Simeon","Alistair","Hamza","Michael","Joab","Brogan","Fahid","Jawad","Danesh","Daniel","Harry","Shameela","Chenyse","Maryama","Jazz","Abdur"]
quirk = ["Fast", "strong", "earth", "Fire", "Water", "Rasengun", "Trump", "Biden", "Super", "batman", "guitar", "surfer", "Hello", "pikachu", "Charizard", "Lapras"]

def add_people():
    connection = connect()
    i = (name[(random.randint(0, len(name) - 1))])
    name.remove(i)
    j = (name[(random.randint(0, len(name) - 1))]) + "_" + (quirk[(random.randint(0, len(name) - 1))])  + "gmail.com"
    cursor = connection.cursor()
    cursor.execute("INSERT INTO e(name_, drink) VALUES (%s,%s)", (i, j) )
    connection.commit()
    cursor.close()
    connection.close()
    holder = Person(n,h) 
    people_list.append(holder)