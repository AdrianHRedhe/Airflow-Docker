from airflow.operators.python import task
from airflow.models import DAG
import datetime as dt
import pandas as pd
import sendEmail
from scrapeCSV import runScrapeAndReturnCSV

# Write the recipient of the email here, I suggest you test it with your own email to try it out.
@task
def retrieveRecipient():
    return ''

# This function actually writes the email. The sender is hardcoded but can be changed in 
# sendEmail.py if you wish to send the email from another email adress.
@task
def send_email_task(recipient_email, subject, message,attachment):
    sendEmail.send_email(recipient_email, subject, message,attachment)

# This function could be used to send an alternative message, as an example,
# it could be used to highlight some information from the Scraped CSV
@task
def retrieveMessage(attachment):
    weatherTomorrow = attachment[attachment['daysFromNow'] == 1]
    maxTemperature = weatherTomorrow.degree.max()
    return f"Here comes your scraped CSV file, tomorrow the highest temperature will be {maxTemperature}. \n"

@task
def retrieveSubject():
    return "This is an email from an Airflow DAG"

# This function runs the scrape that is described in the helper function scrapeCSV.py
# and returns a CSV file with the scraped information.
@task
def retrieveAttachment():
    attachment = runScrapeAndReturnCSV()
    return attachment


with DAG(
   "Email_Me_Info",
   default_args={'owner': 'airflow'},
   start_date=dt.datetime(2023,8,9),
   schedule=None,
   catchup=False
) as dag:
   subject = retrieveSubject()
   recipient_email = retrieveRecipient()
   attachment = retrieveAttachment()
   message = retrieveMessage(attachment)
   
   send_email_task(recipient_email,subject,message,attachment)