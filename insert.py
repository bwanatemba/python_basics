
import sqlite3

conn = sqlite3.connect("example.db")
print("Opened Database Successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(1,'EMOBILIS', '7', 'WESTLANDS', 25000)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(2,'MICROSOFT', '8', 'EASTLANDS', 45000)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(3,'ORACLE', '9', 'NORTHLANDS', 85000)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
    VALUES(4,'GOOGLE', '10', 'SOUTHLANDS', 65000)");

conn.commit()
print("Records Created Successfully!")
conn.close()