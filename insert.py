import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(1,'Jeff',33,'Califorina',5000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(2,'Allen',34,'Norway',25000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(3,'Mark',63,'New York',35000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
             VALUES(4,'Brendah',23,'Kenya',89000.00)")

conn.commit()
print("Records added successfully")
conn.close()