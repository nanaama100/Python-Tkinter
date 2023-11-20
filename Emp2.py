from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import subprocess
from tkinter.ttk import Combobox
import mysql.connector
import re

#connecting the python codes to the database
con = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Office@1000.",
    database = "goldskydb"
)

cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Employees(Full_Name varchar(100), Gender varchar(50), Birth_Date varchar(50), Department varchar(150), Employee_Id varchar(50), Employee_Rate varchar(50), Hire_Date varchar(20), Working_Hours int, Employee_Status varchar(100), Contact_Number varchar(12), Email varchar(200), House_Address varchar(200))")
con.commit()

# #checking the format of the phone number
# cursor.execute("alter table Employees add constraint chkTel check(Contact_Number REGEXP '^[0-9]{3}+[-]+[0-9]{4}+[-]+[0-9]{3}$')")
# con.commit()
# def Chk_Phone(Tel):
#     pattern = '^[0-9]{3}+[-]+[0-9]{4}+[-]+[0-9]{3}$'
#     return re.match(pattern, Tel)


#function to save employee information
def Save_Employee():
    Name = Name_Entry.get()
    Gend = Radio_Ent.get()
    Date_Birth = DOB_Entry.get()
    Department = Dep.get()
    Id = Emp_Id.get()
    Rate = Emp_Rate.get()
    Recruit = Hire.get()
    Work = WK_Hours.get()
    Status = WK_Status.get()
    Tel = Cont.get()
    Mail = Email.get()
    House = H_Address.get("1.0", "end-1c")

    #telling user to fill out all fields
    if Name == "" or Date_Birth == "" or Id == "" or Rate == "" or Recruit == "" or Work == "" or Status == "" or Mail == "" or House == "":
        messagebox.showerror("Error", "Kindly fill out all fields") 
    elif not Tel:
        messagebox.showerror("Error", "Kindly check the format of your phone number")
    elif Department == "Select Department":
        messagebox.showerror("Error", "Kindly select your department")
    elif Gend == "":
        messagebox.showerror("Error", "Kindly select your gender")
    else: 
        Date_Birth = datetime.strptime(Date_Birth,"%Y-%m-%d").date()   #converting the date of birth string to a date object
        Recruit = datetime.strptime(Recruit,"%Y-%m-%d").date()  #converting the employee start date string to a date object

        #Insert the employee data into the database
        cursor.execute("INSERT INTO employees(Full_Name, Gender, Birth_Date, Department, Employee_Id, Employee_Rate, Hire_Date, Working_Hours, Employee_Status, Contact_Number, Email, House_Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Name, Gend, Date_Birth, Department, Id, Rate, Recruit, Work, Status, Tel, Mail, House))
        con.commit()
        messagebox.showinfo("Employee", "Successfully Saved")


#this code creates a new window
window = Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry('1045x665')
window.config(bg="#06283D")
img = PhotoImage(file="Empy4.png") #adding a pic to the window title
window.iconphoto(True,img)

#code for employee pic
new1 = Image.open("PIC3-removebg-preview.png")
new2 = new1.resize((350,210))
new3 = ImageTk.PhotoImage(new2)
new_label = Label(window, image= new3, bg="#06283D")
new_label.place(x=1050, y=140)

#building the head label 
Head_label = Label(window, text= "Employee Registration Form", bg="#06283D", fg="gold", font=("Times New Roman", 40))
Head_label.pack(side=TOP, fill=X)

#creating my first frame
First_Frame = LabelFrame(window, text= "DETAILS 1", font=("Rockwell Condensed", 14), relief= "groove", height= 250, width= 950, bd= 2, bg= "gold")
First_Frame.place(x=70,y=180)

#labels for the first frame
Label(First_Frame, text="Full Name: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=50)
Label(First_Frame, text="Gender: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=100)
Label(First_Frame, text="Date of Birth: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=150)
Label(First_Frame, text="Employee ID: ", font=("Arial", 12), bg= "gold", fg="black").place(x=550, y=50)
Label(First_Frame, text="Department: ", font=("Arial", 12), bg= "gold", fg="black").place(x=550, y=100)
Label(First_Frame, text="Pay Rate: ", font=("Arial", 12), bg= "gold", fg="black").place(x=550, y=150)

#Creating a radio button for the gender category
Name_Entry = Entry(First_Frame, width= 40, font=("Arial", 10))
Name_Entry.place(x=160, y=50)

Radio_Ent = StringVar()
Radio_Lab1 = Radiobutton(First_Frame, variable=Radio_Ent, value="Male", text= "Male", fg="black", bg="gold")
Radio_Lab1.place(x=150, y=100)
Radio_Lab2 = Radiobutton(First_Frame, variable=Radio_Ent, value="Female", text= "Female", fg="black", bg="gold")
Radio_Lab2.place(x=250, y=100)

#creating entry for the date of birth
DOB_Entry = Entry(First_Frame, width= 30, font=("Arial", 10))
DOB_Entry.place(x=160, y=150) 
Small_Label = Label(First_Frame, text= "Enter date (YYYY-MM-DD)", font=("Arial", 10), fg= "black", bg= "gold")
Small_Label.place(x=170, y=180)

#combobox for the department 
Dep = Combobox(First_Frame, values= ["Human Resource", "Public Relations", "Advertising and Creative Department", "Marketing", "Administration", "Non-Official Staff", "IT Department", "Photography and Videography"], font=("Arial", 10), width=27)
Dep.set("Select Department")
Dep.place(x=670, y=100)

#creating entry for employee id
Emp_Id= Entry(First_Frame, width= 30, font=("Arial", 10))
Emp_Id.place(x=670, y=50) 

#creating entry for pay rate
Emp_Rate= Entry(First_Frame, width= 30, font=("Arial", 10))
Emp_Rate.place(x=670, y=150) 

#creating a second frame 
Second_Frame = LabelFrame(window, text= "DETAILS 2", font=("Rockwell Condensed", 14), relief= "groove", height= 220, width= 950, bd= 2, bg= "gold")
Second_Frame.place(x=70,y=465)

#labels for the second frame
Label(Second_Frame, text="Hire Date: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=50)
HS_Label = Label(Second_Frame, text= "Enter date (YYYY-MM-DD)", font=("Arial", 10), fg= "black", bg= "gold")
HS_Label.place(x=170, y=70)
Label(Second_Frame, text="Working Hours: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=100)
Label(Second_Frame, text="Working Status: ", font=("Arial", 12), bg= "gold", fg="black").place(x=30, y=150)
Label(Second_Frame, text="Contact Number: ", font=("Arial", 12), bg= "gold", fg="black").place(x=530, y=50)
CN_Label = Label(Second_Frame, text= "Format; (000-0000-000)", font=("Arial", 10), fg= "black", bg= "gold")
CN_Label.place(x=690, y=70)
Label(Second_Frame, text="Email Address: ", font=("Arial", 12), bg= "gold", fg="black").place(x=530, y=100)
Label(Second_Frame, text="House Address: ", font=("Arial", 12), bg= "gold", fg="black").place(x=530, y=150)

#creating entry for hire day
Hire = Entry(Second_Frame, width= 30, font=("Arial", 10))
Hire.place(x=160, y=50)

#creating entry for Working Hours 
WK_Hours = Entry(Second_Frame, width= 30, font=("Arial", 10))
WK_Hours.place(x=160, y=100)

#creating entry for Working Status
WK_Status = Entry(Second_Frame, width= 30, font=("Arial", 10))
WK_Status.place(x=160, y=150)

#creating entry for Contact Number
Cont = Entry(Second_Frame, width= 30, font=("Arial", 10))
Cont.place(x=670, y=50)

#creating entry for email
Email = Entry(Second_Frame, width= 35, font=("Arial", 10))
Email.place(x=670, y=100)

#creating entry for house address
H_Address = Text(Second_Frame, width= 38, height= 2, font=("Arial", 10))
H_Address.place(x=670, y=150)

#a button that submits all the employee info
Save_Button = Button(window, text= "SAVE", font=("Times New Roman", 14), bd= 5, width=12, relief="groove", fg="black", bg="green", command=Save_Employee)
Save_Button.place(x=1150, y=420)


#function to clear all info from entries
def Clearing_Entries():
    Name_Entry.delete(0, END)
    Radio_Ent.set("")
    DOB_Entry.delete(0, END)
    Dep.set("Select Department")
    Emp_Id.delete(0, END)
    Emp_Rate.delete(0, END)
    Hire.delete(0, END)
    WK_Hours.delete(0, END)
    WK_Status.delete(0, END)
    Cont.delete(0, END)
    Email.delete(0, END)
    H_Address.delete(1.0, END)

#button to clear all employee info
Clear_Button = Button(window, text= "CLEAR", font=("Times New Roman", 12), bd= 5, width=12, relief="groove", fg="black", bg="gold", command= Clearing_Entries)
Clear_Button.place(x=1150, y=500)


def Previous_Page():
    window.withdraw()
    subprocess.Popen(["python", "Emp1.py"])

#button to return to previous page
Exit_Button = Button(window, text= "EXIT", font=("Times New Roman", 12), bd= 5, width=12, relief="groove", fg="black", bg="grey", command=Previous_Page)
Exit_Button.place(x=1150, y=570)

window.mainloop()



