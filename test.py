import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "alex",
password = "",
database="testdb"
)
mycursor = mydb.cursor()
sqlFormula = "insert into students (name , age )values (%s, %s)"

students = [("lamken" , 22),
                ("puffy", 24),
                ("Jacob", 12),
                ("Randomgee", 25),
                ("Yvonne", 20)]

mycursor.execute(sqlFormula, students);
mydb.commit();
