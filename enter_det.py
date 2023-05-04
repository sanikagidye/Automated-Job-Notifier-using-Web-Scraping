import subprocess
import threading
import tkinter
from tkinter import *
from tkinter import messagebox, IntVar
import pymysql
from threading import Thread

add_window = tkinter.Tk()
add_window.geometry('600x450+500+50')
add_window.title('Details')

def scrape():
    import scrape2



def clear():
    job_e.delete(0,END)
    loc_e.delete(0,END)

def connect_database():
    if job_e.get() == '' or loc_e.get() == '' :
        messagebox.showerror('Error', 'All field are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Minnu%1122')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue.Please Try Again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s'
        mycursor.execute(query, (un_e.get()))
        row = mycursor.fetchone()
        n3 = row[0]

        query = 'use userdata'
        mycursor.execute(query)
        query = 'insert into details(id,job_name, Location) values(%s,%s,%s)'
        mycursor.execute(query, (n3,job_e.get(), loc_e.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Added successful')
        clear()
        back()

def back():
    add_window.destroy()
    #import home

heading = Label(add_window, text='Add Details', font=('Helvetica', 23, 'bold'), bg='white', fg='purple')
heading.grid(row=0, column=0, padx=10, pady=10)

un = Label(add_window, text='Username', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
un.grid(row=3, column=0, padx=25, pady=10)

un_e = Entry(add_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
un_e.grid(row=3, column=1, padx=25)

job_l = Label(add_window, text='Job Title', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
job_l.grid(row=5, column=0, padx=25, pady=10)

job_e = Entry(add_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
job_e.grid(row=5, column=1, padx=25)

loc_l = Label(add_window, text='Location', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
loc_l.grid(row=7, column=0, padx=25, pady=10)

loc_e = Entry(add_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
loc_e.grid(row=7, column=1, padx=25)

signupButton = Button(add_window, text='ADD', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=threading.Thread(target=lambda:[connect_database(),scrape()]).start)

signupButton.grid(row=10, column=0, pady=10)

backButton = Button(add_window, text='Back', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=back)

backButton.grid(row=10, column=1, pady=10)

add_window.mainloop()