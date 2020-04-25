from tkinter import *
import mysql.connector

root =Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter you name") #placeholder of textbox 

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
myButton = Button(root, text="Enter your name!", padx=20, pady=20, command = myClick)
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
