#This code now updates the employee information............
from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import subprocess
from tkinter.ttk import Combobox

con = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Office@1000.",
    database = "goldskydb"    
)

cursor = con.cursor()

def Updating_Employee():
    employee_id = Emp_Id.get()
    field = field_lbl.get()
    new_value = Val_Entry.get()

    query = f"UPDATE employees SET {field} = %s WHERE Employee_Id = %s"
    values = (new_value, employee_id)
    cursor.execute(query,values)
    con.commit()

    result_lbl.config(text="Employee Information Updated Successfully")


#this code creates a new window
window = Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry('1046x588')
window.config(bg="#06283D")
img = PhotoImage(file= "Empy4.png")
window.iconphoto(True,img)

#code for employee pic
new1 = Image.open("PIC9-removebg-preview.png")
new2 = new1.resize((170,140))
new3 = ImageTk.PhotoImage(new2)
new_label = Label(window, image= new3, bg="#06283D")
new_label.place(x=10, y=3)

# #label for heading
# Update_label = Label(window, text= "Updating Employee Information", font= ("Rockwell Condensed",38), bg="#06283D", fg="gold")
# Update_label.place(x=210, y=25)

#label for results
result_lbl = Label(window, text="", font=("Arial(Body)", 18), fg= "gold", bg="#06283D")
result_lbl.place(x=200, y=170)


#label for frame
new_frame = LabelFrame(window, bg="gold", relief="groove", width= 700, height= 470)
new_frame.place(x=200, y=200)

#label for instruction
Inst = Label(new_frame, bg="gold", font=("Calibri Light (Headings)", 14), fg="black", text="Kindly fill out fields to update employee info").place(x=40, y=10)

#Label and entry box
A_label = Label(new_frame, text= "Employee ID", font=("Arial Narrow", 14), fg= "black", bg="gold").place(x=50, y=130)
Emp_Id = Entry(new_frame, width= 40, font=("Times New Roman", 13), fg="black", bg="white")
Emp_Id.place(x=200, y=125)

#combobox for the department 
lbl = Label(new_frame, text="Update Field", font=("Arial Narrow",14), fg="black", bg="gold").place(x=50, y=200)
field_lbl = Combobox(new_frame, values= ["Full_Name", "Gender", "Birth_Date", "Department", "Employee_Id", "Employee_Rate", "Hire_Date", "Working_Hours", "Employee_Status", "Contact_Number", "Email", "House_Address"], font=("Arial", 10), width=40, height=6)
field_lbl.set("select field")
field_lbl.place(x=200, y=200)

#Label and entry box
Val_label = Label(new_frame, text= "New Value", font=("Arial Narrow", 14), fg= "black", bg="gold").place(x=50,y=290)
Val_Entry = Entry(new_frame, width= 40, font=("Times New Roman", 14), fg="black", bg="white")
Val_Entry.place(x=200, y=285)


#a button that updates employee info
Save_Button = Button(window, text= "UPDATE", font=("Times New Roman", 14), bd= 5, relief="groove", fg="black", bg="green", command=Updating_Employee)
Save_Button.place(x=1000, y=620)

def Clearing_Entries():
    Emp_Id.delete(1.0, END)
    field_lbl.set("Select Field")
    Val_Entry.delete(1.0, END)

    
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
