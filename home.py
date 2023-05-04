import tkinter
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox



home_window = tkinter.Tk()
home_window.geometry('925x700+300+50')
home_window.title('Home Page')

background = ImageTk.PhotoImage(file='vector.png')
bgLabel = Label(home_window, image=background)
bgLabel.grid()

frame = Frame(home_window)
frame.place(x=700, y=50)

def logout():
    home_window.destroy()
    messagebox.showinfo('Success', 'LoggedOut successfully')
    import login

def delete():
    #home_window.destroy()
    import delete_acc


def det():
    #home_window.destroy()
    import enter_det

def edit():
    #home_window.destroy()
    import edit_det

b1 = Button(frame, text='Enter Details', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=17,height=5, cursor='hand2',command=det)
b1.grid(row=5, column=30, pady=10)


b2 = Button(frame, text='Edit Details', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=17,height=5, cursor='hand2',command=edit)
b2.grid(row=7, column=30, pady=10)

b3 = Button(frame, text='Logout', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=17,height=5, cursor='hand2',command=logout)
b3.grid(row=9, column=30, pady=10)

b4 = Button(frame, text='Delete Account', font=('Helvetica', 16, 'bold'), bd=0, bg='DodgerBlue4', fg='white',
                      activebackground='DodgerBlue4', activeforeground='white', width=17,height=5, cursor='hand2',command=delete)
b4.grid(row=11, column=30, pady=10)



home_window.mainloop()
