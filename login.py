from tkinter import *
from tkinter import Tk, mainloop
from tkinter import messagebox
import pymysql

#from PIL import ImageTk,Image
#import ast

def login_user():
    if username.get()=='' or password.get()=='':
        messagebox.showerror('Error','All fields required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Minnu%1122')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection error')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(username.get(),password.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')

        else:
            messagebox.showinfo('Success','Login is successful')
            window.destroy()
            import home

def signup_page():
    window.destroy()
    import signup

def user_enter(event):
    if username.get()=='Username':
        username.delete(0,END)

def password_enter(event):
    if password.get()=='Password':
        password.delete(0,END)

def hide():
    open_eye.config(file='hide.png')
    password.config(show='*')
    eyeButton.config(command=show)

def show():
    open_eye.config(file='show.png')
    password.config(show='')
    eyeButton.config(command=hide)

window=Tk()
window.title("SIGNUP")
window.geometry('925x700+300+50')
window.title('Login Page')

img=PhotoImage(file="vector.png")
Label(window,image=img,border=0,bg='white smoke').place(x=50,y=90)

heading= Label(window,text='USER  LOGIN', font=('Helvetica', 23, 'bold'), bg='white', fg='steel blue')
heading.place(x=630,y=50)

username=Entry(window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='steel blue',bg='#D9D8D7')
username.place(x=600,y=150)
username.insert(0,'Username')
username.bind('<FocusIn>',user_enter)

Frame(window,width=300,height=2,bg='steel blue').place(x=600,y=182)

password=Entry(window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='steel blue',bg='#D9D8D7')
password.place(x=600,y=210)
password.insert(0,'Password')
password.bind('<FocusIn>',password_enter)

Frame(window,width=300,height=2,bg='steel blue').place(x=700,y=242)


open_eye=PhotoImage(file='show.png',)
eyeButton= Button(window,image=open_eye,cursor='hand2',command=hide)
eyeButton.place(x=870,y=210)


login_button = Button(window,text="Login",font=('Helvetica',16,'bold'),bd=0,bg='DodgerBlue4',fg='white',activebackground='DodgerBlue4',activeforeground='white',width=23,cursor='hand2',command=login_user)
login_button.place(x=600,y=350)

signup_label = Button(window,text="Don't have an account?",font=('Helvetica',9,'bold'),bd=0,fg='DodgerBlue4',bg='white')
signup_label.place(x=600,y=400)

create_button = Button(window,text="Create new one",font=('Helvetica',9,'bold'),bd=0,bg='white',fg='blue',activebackground='white',activeforeground='blue',cursor='hand2',command=signup_page)
create_button.place(x=800,y=400)

window.mainloop()