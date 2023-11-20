from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

#this code creates a new window
window = Tk()
window.title("EMPLOYEE MANAGEMENT SYSTEM")
window.geometry('1045x665')
window.config(bg="#06283D")
img = PhotoImage(file="Empy4.png") #adding a pic to the window title

window.iconphoto(True,img)

#code for employee pic
new1 = Image.open("PIC9-removebg-preview.png")
new2 = new1.resize((150,130))
new3 = ImageTk.PhotoImage(new2)
new_label = Label(window, image= new3, bg="#06283D")
new_label.place(x=100, y=5)

Head_Label= Label(window, text= "GoldSky-IT Employee Management System", bg="#06283D",fg="gold", font=("Rockwell Condensed", 45))
Head_Label.place(x=300,y=35)

#this code calls the code for the employee form.
def Adding_Employee():
    window.withdraw()
    subprocess.Popen(["python", "Emp2.py"])

Add_Emp_Button = Button(window, text="Add Employee", font=("Arial Black", 11), relief="groove", bd=8, width= 50, bg="gold", command= Adding_Employee)
Add_Emp_Button.place(x=350, y=230)

#this code calls the code for updating the employee. 
def Updating_Employee():
    window.withdraw()
    subprocess.Popen(["python", "Emp3.py"])

Update_Emp_Button = Button(window, text="Update Employee Information", font=("Arial Black", 11), relief="groove", bd=8, width= 50, bg="gold", command= Updating_Employee)
Update_Emp_Button.place(x=350, y=320)

def All_Employees():
    window.withdraw()
    subprocess.Popen(["python", "Emp4.py"])

View_Employee = Button(window, text="View All Employees", font=("Arial Black", 11), relief="groove", bd=8, width= 50, bg="gold", command=All_Employees)
View_Employee.place(x=350, y=410)


Remove_Employee = Button(window, text="Remove Employee", font=("Arial Black", 11), relief="groove", bd=8, width= 50, bg="gold")
Remove_Employee.place(x=350, y=500)


Exit = Button(window, text="Exit", font=("Arial Black", 11), relief="groove", bd=8, width= 50, bg="gold", command= window.destroy)
Exit.place(x=350, y=590)



window.mainloop()