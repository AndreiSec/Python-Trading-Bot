'''
Created on Oct 2, 2020

@author: andrei
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Email Account
email_sender_account = "KMD SOUNDS"
email_sender_username = "kmdsounds@gmail.com"
email_sender_password = "!Tradingbot123"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = 587

#Email Content
email_recepients = ["andreisecara01@gmail.com", "tavi@thisisthequestion.com"]
email_subject = "Stocks that opened 5% below close."
# email_body = "<html of your body here>"


l = [1,2,3,4,5,6,7,8]

def send_email(email_body):
    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    
    email_body = str(email_body)
    for recipient in email_recepients:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative')
        message['From'] = email_sender_account
        message['To'] = recipient
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'html'))
        text = message.as_string()
        server.sendmail(email_sender_account,recipient,text)
    
    server.quit()
    

