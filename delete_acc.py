import tkinter
from tkinter import *
from tkinter import messagebox, IntVar
import pymysql

del_window = tkinter.Tk()
del_window.geometry('600x300+500+70')
del_window.title('Delete Account')

def back():
    del_window.destroy()
    import home

def connect_database():
    if  un_e.get() == '' :
        messagebox.showerror('Error', 'Kindly enter Username')
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


        sql_update_query = """Delete from details where id = %s"""
        input_data = (n2)
        mycursor.execute(sql_update_query, input_data)
        con.commit()
        sql_update_query = """Delete from data where id = %s"""
        input_data = (n2)
        mycursor.execute(sql_update_query, input_data)
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Account Deleted successful')
        del_window.destroy()
        import signup


un = Label(del_window, text='Confirm your Username', font=('Microsoft Yahei UI Light', 15, 'bold'), bg='white')
un.grid(row=3, column=0, padx=25, pady=10)

un_e = Entry(del_window, width=28, font=('Microsoft Yahei UI Light', 15, 'bold'))
un_e.grid(row=8, column=0, padx=25)

signupButton = Button(del_window, text='Confirm', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=connect_database)

signupButton.grid(row=10, column=0, pady=10)

backButton = Button(del_window, text='Cancel', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=13, cursor='hand2',command=back)

backButton.grid(row=10, column=1, pady=10)

del_window.mainloop()