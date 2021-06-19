import datetime as dt
import time
import smtplib
import json

def send_email():
    with open(r"C:\Users\DELL\Downloads\json_mail.json")as f:
        data=json.load(f)
        gmailaddress = 'sender_mail@gmail.com'
        gmailpassword = 'password'
        mailto = data['email_ids']
        SUBJECT='SD TEAM 5'
        msg=data['subject']
        message = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, mailto , message)
        mailServer.quit()

def send_email_at(send_time):
    send_email()
    print('email sent')
    time.sleep(60*30) 

first_email_time = dt.datetime(2021,6,13,21,0,0) 
interval = dt.timedelta(minutes=1*1)

send_time = first_email_time
while True:
    send_time = send_time + interval
    send_email_at(send_time)