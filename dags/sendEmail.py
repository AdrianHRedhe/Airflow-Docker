import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd

# This function sends and email to the the recipient email
# The sender email is hardcoded, but easily interchangable
# if you wish to make a function where the email can be 
# changed.

def send_email(recipient_email, subject, message, attachment=None):
    # Provide your Gmail credentials and the email details
    sender_email = '1234.airflow.example@gmail.com'
    sender_password = 'qtgexzgqsbggydxm'
    
    # Here you can replace the email with your own if you want the program to send an email
    recipient_email = str(recipient_email)
    subject = str(subject)
    message = str(message)

    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a secure connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to your Gmail account
    server.login(sender_email, sender_password)

    # Create the email message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'plain'))

    # If you have a csv attachment add it to the email.
    if attachment is not None:
        csv_attachment = MIMEApplication(attachment.to_csv())
        csv_attachment.add_header('Content-Disposition','attachment; filename='+ 'weatherdata.csv')

        email_message.attach(csv_attachment)

    # Send the email
    server.send_message(email_message)

    # Disconnect from the server
    server.quit()