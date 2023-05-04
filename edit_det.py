import tkinter
from tkinter import *
from tkinter import messagebox, IntVar
import pymysql
import threading

edit_window = tkinter.Tk()
edit_window.geometry('600x450+500+50')
edit_window.title('Details')

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
        n2=str(n3)

        sql_update_query = """Update details set job_name = %s,Location = %s where id = %s"""
        input_data = (job_e.get(),loc_e.get(),n2)
        mycursor.execute(sql_update_query, input_data)
        con.commit()
        messagebox.showinfo('Success', 'Updated successful')
        clear()
        con.commit()
        con.close()
        back()


def back():
        edit_window.destroy()
        #import home

heading = Label(edit_window, text='Edit Details', font=('Helvetica', 23, 'bold'), bg='white', fg='purple')
heading.grid(row=0, column=0, padx=10, pady=10)

un = Label(edit_window, text='Username', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
un.grid(row=3, column=0, padx=25, pady=10)

un_e = Entry(edit_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
un_e.grid(row=3, column=1, padx=25)

job_l = Label(edit_window, text='Job Title', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
job_l.grid(row=5, column=0, padx=25, pady=10)

job_e = Entry(edit_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
job_e.grid(row=5, column=1, padx=25)

loc_l = Label(edit_window, text='Location', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
loc_l.grid(row=7, column=0, padx=25, pady=10)

loc_e = Entry(edit_window, width=25, font=('Microsoft Yahei UI Light', 15, 'bold'))
loc_e.grid(row=7, column=1, padx=25)

signupButton = Button(edit_window, text='Update', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=threading.Thread(target=lambda:[connect_database(),scrape()]).start)

signupButton.grid(row=10, column=0, pady=10)

backButton = Button(edit_window, text='Back', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=back)

backButton.grid(row=10, column=1, pady=10)

edit_window.mainloop()