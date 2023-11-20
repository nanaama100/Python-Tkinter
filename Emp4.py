from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import mysql.connector
from tkinter import ttk

#this code creates a new window
window = Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry('1045x665')
window.config(bg="#06283D")
img = PhotoImage(file="Empy4.png") #adding a pic to the window title
window.iconphoto(True,img)


connect = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Office@1000.",
    database = "goldskydb"    
)

conn = connect.cursor()  

# Retrieving all employees from the database.
query = "Select * from Employees"
conn.execute(query)

tree = ttk.Treeview(window)

#defining the number of columns
tree ["columns"] = ("Full_Name", "Gender", "Birth_Date", "Department", "Employee_Id", "Employee_Rate", "Hire_Date", "Working_Hours", "Employee_Status", "Contact_Number", "Email", "House_Address")

#removing the empty space in the result of the view of all employees
tree['show'] = 'headings'

#Assigning the width, minwidth and anchor to the respective columns
tree.column("Full_Name", width= 200, minwidth= 200, anchor= CENTER)
tree.column("Gender", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Birth_Date", width= 100, minwidth= 100, anchor= CENTER)
tree.column("Department", width= 200, minwidth= 200, anchor= CENTER)
tree.column("Employee_Id", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Employee_Rate", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Hire_Date", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Working_Hours", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Employee_Status", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Contact_Number", width= 150, minwidth= 150, anchor= CENTER)
tree.column("Email", width= 200, minwidth= 200, anchor= CENTER)
tree.column("House_Address", width= 250, minwidth= 250, anchor= CENTER)


#Assigning the heading names to the respective columns 
tree.heading("Full_Name", text= "Full Name", anchor= CENTER)
tree.heading("Gender", text= "Gender", anchor= CENTER)
tree.heading("Birth_Date", text= "Date of Birth", anchor= CENTER)
tree.heading("Department", text= "Employee Department", anchor= CENTER)
tree.heading("Employee_Id", text= "Employee Id", anchor= CENTER)
tree.heading("Employee_Rate", text= "Employee Rate", anchor= CENTER)
tree.heading("Hire_Date", text= "Hire Date", anchor= CENTER)
tree.heading("Working_Hours", text= "Working Hours", anchor= CENTER)
tree.heading("Employee_Status", text= "Employee Status", anchor= CENTER)
tree.heading("Contact_Number", text= "Telephone Number", anchor= CENTER)
tree.heading("Email", text= "Email", anchor= CENTER)
tree.heading("House_Address", text= "House Address", anchor= CENTER)

i = 0
for ro in conn:
    tree.insert('', i, text= "", values= (ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10], ro[11]))       
    i= i+1 
tree.pack()
#tree.place(x=10, y=150)

#theme for the columns
s = ttk.Style(window)
s.theme_use("classic")

#setting background colour and font of heading
s.configure("Treeview.Heading", background = "#06283D", foreground = "white", font = ("Arial", 12, "bold"))

#creating a horizontal scrollbar
scroll = ttk.Scrollbar(window, orient="horizontal")

scroll.configure(command=tree.xview)
tree.configure(xscrollcommand = scroll.set)
scroll.pack(fill=X, side= BOTTOM)





window.mainloop()