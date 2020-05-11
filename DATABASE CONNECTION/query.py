import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT ID,NAME,CITY,COMMISSION from SALESMAN")
for row in cursor:
 print("ID :: ", row[0])
 print("NAME :: ", row[1])
 print("CITY :: ", row[2])
 print("COMMISSION :: ", row[3], "\n")
print("Operation done successfully");
print("---------------------------");
conn.execute("UPDATE CUSTOMER set GRADE = 2500 where CUS_ID = 100")

print("Updated succesfully")
print("---------------------------");
conn.commit()
cursor = conn.execute("SELECT cus_id, cus_name, city, grade from CUSTOMER")
for row in cursor:
 print("ID :: ", row[0])
 print("NAME :: ", row[1])
 print("CITY :: ", row[2])
 print("GRADE :: ", row[3], "\n")
print("Operation done successfully");
print("---------------------------");




print ("Operation done successfully");
conn.close()