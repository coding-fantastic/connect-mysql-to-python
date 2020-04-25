from tkinter import *
import mysql.connector

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
        myLabel2 =Label(root, text=row)
        myLabel2.pack()


root =Tk()

e = Entry(root, width = 50)
e.pack()

 #placeholder of textbox
#e.insert(0, "Enter you name")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
myButton = Button(root, text="Enter your name!", padx=20, pady=20, command = myClick)
myButton.pack()

myButton = Button(root, text ="Click the button to display all entries in students table" ,command=db )
myButton.pack()
#create an event loop
root.mainloop()
