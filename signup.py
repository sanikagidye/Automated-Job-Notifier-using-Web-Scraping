import tkinter
from tkinter import *
from tkinter import messagebox, IntVar
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)



def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All field are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms and Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Minnu%1122')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue.Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20) )'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query ='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'Username Already exists')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration successful')
            clear()
            signup_window.destroy()
            import login


def login_page():
    signup_window.destroy()
    import login


signup_window = tkinter.Tk()
signup_window.geometry('925x700+300+50')
signup_window.title('Signup Page')
background = ImageTk.PhotoImage(file='vector.png')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window)
frame.place(x=480, y=50)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Helvetica', 23, 'bold'), bg='white', fg='blue')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25)

passwordEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25)

confirmEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check=IntVar()
termsandcondition = Checkbutton(frame, text='I agree to the Terms and Conditions',
                                font=('Microsoft Yahei UI Light', 10, 'bold'), cursor='hand2',variable=check)
termsandcondition.grid(row=9, column=0, pady=10, padx=15)

signupButton = Button(frame, text='Signup', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=17, cursor='hand2',
                      command=connect_database)

signupButton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text='Have an account?', font=('Helvetica', 10, 'bold'), bg='white', fg='DodgerBlue4')

alreadyaccount.grid(row=11, column=0, padx=25, sticky='w')

loginButton = Button(frame, text='Login', font=('Helvetica', 9, 'bold underline'), bd=0, bg='white', fg='DodgerBlue4',
                     activebackground='white', activeforeground='DodgerBlue4', cursor='hand2', command=login_page)

loginButton.place(x=170, y=446)

signup_window.mainloop()
