import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE SALESMAN
 (ID INT PRIMARY KEY NOT NULL,
 NAME TEXT NOT NULL,
 CITY TEXT NOT NULL,
 COMMISSION REAL);''')
print("Table created successfully")
conn.execute('''CREATE TABLE CUSTOMER
 (CUS_ID INT PRIMARY KEY NOT NULL,
 CUS_NAME TEXT NOT NULL,
 CITY TEXT NOT NULL,
 GRADE REAL);''')
print("Table created successfully")
conn.execute('''CREATE TABLE ORDERS
 (ORDER_NO INT PRIMARY KEY NOT NULL,
 PUR_AMT INT NOT NULL,
 ORDER_DTE TEXT NOT NULL,
 CUSTOMER_ID INT);''')
print("Table created successfully")
conn.commit()
print("Records commited")
conn.close()