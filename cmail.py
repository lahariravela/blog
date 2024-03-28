import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('lahari.ravela@gmail.com','gmho oeua xelk kvbi')
    msg=EmailMessage()
    msg['From']='lahari.ravela@gmail.com'
    msg['subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()