import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'alex',
password = '',
database="testdb"
)
mycursor = mydb.cursor()
mycursor.execute("create table students (name varchar(255), age integer(10))")

for db in mycursor:
    print(db)
