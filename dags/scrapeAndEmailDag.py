from airflow.operators.python import task
from airflow.models import DAG
import datetime as dt
import pandas as pd
from random import randint
import sendEmail

# Write the recipient of the email here, I suggest you test it with your own email to try it out.
@task
def retrieveRecipient():
    return ''

# This function actually writes the email. The sender is hardcoded but can be changed in 
# sendEmail.py if you wish to send the email from another email adress.
@task
def send_email_task(recipient_email, subject, message,attachment):
    sendEmail.send_email(recipient_email, subject, message,attachment)

# I will add the scraping function here later on.
@task
def retrieveMessage():
    return f"This is your random number between 1 and 10: {randint(1,10)}"

@task
def retrieveSubject():
    return "This is an email from an Airflow DAG"

@task
def retrieveAttachment():
    return pd.DataFrame({'TestData':[1,2,3,4,5]})


with DAG(
   "Email_Me_Info",
   default_args={'owner': 'airflow'},
   start_date=dt.datetime(2023,8,9),
   schedule=None,
   catchup=False
) as dag:
   message = retrieveMessage()
   subject = retrieveSubject()
   recipient_email = retrieveRecipient()
   attachment = retrieveAttachment()
   
   send_email_task(recipient_email,subject,message,attachment)