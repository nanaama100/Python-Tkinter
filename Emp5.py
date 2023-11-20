from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from tkinter.ttk import Combobox
import mysql.connector


con = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Office@1000.",
    database = "goldskydb"    
)

def Remove_Employee():
    field = field_combobox.get()
    value = value_entry.get()

    cursor = con.cursor()

    delete_query = f"DELETE FROM employees WHERE {field} = %s"
    value = (value,)
    cursor.execute(delete_query, value)
    con.commit()

    if cursor.rowcount > 0:
        result_label.config(text = "Employee Removed Successfully")
    else:
        result_label.config(text = "Employee Not Found")

    cursor.close()


# #this code creates a new window
window = Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry('1045x665')
window.config(bg="#06283D")
img = PhotoImage(file="Empy4.png") #adding a pic to the window title
window.iconphoto(True,img)

#code for employee pic
new1 = Image.open("PIC9-removebg-preview.png")
new2 = new1.resize((170,140))
new3 = ImageTk.PhotoImage(new2)
new_label = Label(window, image= new3, bg="#06283D")
new_label.place(x=10, y=3)

#label for results
result_label = Label(window, text="", font=("Arial(Body)", 18), fg= "gold", bg="#06283D")
result_label.place(x=200, y=170)

#label for frame
new_frame = LabelFrame(window, bg="gold", relief="groove", width= 700, height= 470)
new_frame.place(x=200, y=200)

#creating id field label
field_label = Label(new_frame, text= "Field: ",font=("Arial Narrow",14), fg="black", bg="gold")
field_label.place(x=50, y=200)

#creating field Combobox
field_combobox = Combobox(new_frame, values= ["Full_Name", "Gender", "Birth_Date", "Department", "Employee_Id", "Employee_Rate", "Hire_Date", "Working_Hours", "Employee_Status", "Contact_Number", "Email", "House_Address"], font=("Arial", 10), width=40, height=6)
field_combobox.place(x=200, y=200)

#value label
value_label = Label(new_frame, text= "Employee ID: ",  font=("Arial Narrow", 14), fg= "black", bg="gold")
value_label.place(x=50,y=120) 

value_entry = Entry(new_frame, width= 40, font=("Times New Roman", 13), fg="black", bg="white")
value_entry.place(x=200, y=120)

#instrction label
Instruct = Label(new_frame, text="Kindly fill out each field", font=("Arial(Body), 14"), fg="black", bg="gold").place(x=10, y=5)

#a button that updates employee info
Remove_Button = Button(window, text= "REMOVE", font=("Times New Roman", 14), bd= 5, relief="groove", fg="black", bg="green", command=Remove_Employee)
Remove_Button.place(x=1000, y=620)

def Clearing_Entries():
    value_entry.delete(1.0, END)
    field_combobox.set("Select Field")

    
#button to clear all employee info
Clear_Button = Button(window, text= "CLEAR", font=("Times New Roman", 12), bd= 7, relief="groove", fg="black", bg="gold", command= Clearing_Entries)
Clear_Button.place(x=1130, y=620)

def Previous_Page():
    window.withdraw()
    subprocess.Popen(["python", "Emp1.py"])

#button to return to previous page
Exit_Button = Button(window, text= "EXIT", font=("Times New Roman", 12), bd= 7, relief="groove", fg="black", bg="grey", command= Previous_Page)
Exit_Button.place(x=1230, y=620)








window.mainloop()