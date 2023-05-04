import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox, IntVar
import pymysql

def send(n1):

    try:
        con = pymysql.connect(host='localhost', user='root', password='Minnu%1122')
        mycursor = con.cursor()

    except:
        messagebox.showerror('Error', 'Database Connectivity Issue.Please Try Again')
    query='use userdata'
    mycursor.execute(query)
    query='SELECT email FROM data where id=%s;'
    mycursor.execute(query,n1)
    row = mycursor.fetchone()
    n3 = row[0]
    n2 = str(n3)
    con.commit()
    con.close()




    sender_add='aksharaminnu1@gmail.com'
    receiver_add=f'{n2}'
    password='yftzqcnkqfplufmz'

    message = MIMEMultipart()

    message['Subject'] = "Your Job Vacancies"
    file = "Vacancies.xlsx"
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(obj)
    my_message = message.as_string()

    email_session=smtplib.SMTP("smtp.gmail.com",587)
    email_session.ehlo()

    email_session.starttls()
    email_session.ehlo()

    email_session.login(sender_add,password)

    email_session.sendmail(sender_add,receiver_add,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")