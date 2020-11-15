import pymysql
import csv

def connect():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='PASSWORD',
                                db='rice',
                                port = 3306,
                                charset='utf8mb4',
    )
