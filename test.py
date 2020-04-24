import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'alex',
password = '',
database="testdb"
)
mycursor = mydb.cursor()
mycursor.execute("show databases")

for db in mycursor:
    print(db)
