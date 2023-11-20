from customtkinter import *
from customtkinter import CustomTkinter
from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

app = CTk()
app.geometry('1045x665')
app.title("Employee Management System")
app.config(bg="#06283D")

#code for employee pic
new1 = Image.open("PIC9-removebg-preview.png")
new2 = new1.resize((150,130))
new3 = ImageTk.PhotoImage(new2)
new_label = Label(master=app, image= new3, bg="#06283D")
new_label.place(x=100, y=5)

Head_Label= CTkLabel(master=app, text_color="gold", text= "GoldSky-IT Employee Management System", bg_color="#06283D", font=("Rockwell Condensed", 45))
Head_Label.place(x=300,y=35)

#this code calls the code for the employee form.
def Adding_Employee():
    app.withdraw()
    subprocess.Popen(["python", "Emp2.py"])

Add_Emp_Button = CTkButton(master=app, text="Add Employee", text_color= "black", font=("Arial(Body)", 15), corner_radius=50, fg_color="gold", command= Adding_Employee)
Add_Emp_Button.set_relief("groove")
Add_Emp_Button.place(x=200, y=450)



app.mainloop()