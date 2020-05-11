import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute("INSERT INTO SALESMAN (ID,NAME,CITY,COMMISSION) \
 VALUES (1, 'Alice', 'Banglore', 2000.00 )");
conn.execute("INSERT INTO SALESMAN (ID,NAME,CITY,COMMISSION) \
 VALUES (2, 'Bob', 'Bangalore', 3000.00 )");
conn.execute("INSERT INTO SALESMAN (ID,NAME,CITY,COMMISSION) \
 VALUES (3, 'Shivani', 'Bidar', 4000.00 )");
print("Records created successfully");
conn.execute("INSERT INTO CUSTOMER\
(CUS_ID,CUS_NAME,CITY,GRADE) \
 VALUES (100, 'XyZ', 'Banglore', 100 )");
conn.execute("INSERT INTO CUSTOMER\
(CUS_ID,CUS_NAME,CITY,GRADE) \
 VALUES (200, 'Bill', 'Banglore', 200)");
conn.execute("INSERT INTO CUSTOMER\
(CUS_ID,CUS_NAME,CITY,GRADE) \
 VALUES (300, 'Gates', 'ranchi', 100 )");
conn.execute("INSERT INTO CUSTOMER\
(CUS_ID,CUS_NAME,CITY,GRADE) \
 VALUES (400, 'Spiderman', 'bangalore', 300)");
print("Records created successfully");
conn.execute("INSERT INTO ORDERS\
(ORDER_NO,PUR_AMT,ORDER_DTE,CUSTOMER_ID) \
 VALUES (1000,2000,'23-04-2020', 200)");
conn.execute("INSERT INTO ORDERS\
(ORDER_NO,PUR_AMT,ORDER_DTE,CUSTOMER_ID) \
 VALUES (2000,3000,'20-04-2020', 100)");
conn.execute("INSERT INTO ORDERS\
(ORDER_NO,PUR_AMT,ORDER_DTE,CUSTOMER_ID) \
 VALUES (3000,2000,'21-04-2020', 100)");
conn.execute("INSERT INTO ORDERS\
(ORDER_NO,PUR_AMT,ORDER_DTE,CUSTOMER_ID) \
 VALUES (4000,1000,'18-04-2020', 200)");
conn.commit()
print("Records created successfully");