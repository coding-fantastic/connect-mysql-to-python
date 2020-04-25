from tkinter import *
import mysql.connector

root =Tk()
#creating a label widget
myLabel =Label(root, text="Hello World!")

#shoving it onto the screen
myLabel.pack()

#create an event loop
root.mainloop()


def db():


    mydb = mysql.connector.connect(
    host = "localhost",
    user = "alex",
    password = "",
    database="testdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute('select * from students where name like "%eff%"' )
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
