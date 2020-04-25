from tkinter import *
import mysql.connector

root =Tk()

def myClick():
    myLabel = Label(root, text="look! i clicked a  button")
    myLabel.pack()
myButton = Button(root, text="Click Me!", padx=50, pady=100, command = myClick)
myButton.pack()

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
