from airflow.operators.python import task
from airflow.models import DAG
import datetime as dt
import pandas as pd
from send_email import send_email
from scrape import run_scrape_and_return_df

# Write the recipient of the email here, I suggest you test it with your own email to try it out.
@task
def retrieve_recipient():
    recipient_email = ''
    return recipient_email

# This function actually writes the email. The sender is hardcoded but can be changed in 
# sendEmail.py if you wish to send the email from another email adress.
@task
def send_email_task(recipient_email, subject, message,attachment):
    send_email(recipient_email, subject, message,attachment)

# This function could be used to send an alternative message, as an example,
# it could be used to highlight some information from the Scraped CSV
@task
def retrieve_message(attachment):
    weather_tomorrow = attachment[attachment['daysFromNow'] == 1]
    max_temperature = weather_tomorrow.degree.max()
    return f"Here comes your scraped CSV file, tomorrow the highest temperature will be {max_temperature}. \n"

@task
def retrieve_subject():
    return "This is an email from an Airflow DAG"

# This function runs the scrape that is described in the helper function scrapeCSV.py
# and returns a CSV file with the scraped information.
@task
def retrieve_attachment():
    attachment = run_scrape_and_return_df()
    return attachment


with DAG(
   "Scrape_And_Email_Me_Info",
   default_args={'owner': 'airflow'},
   start_date=dt.datetime(2023,8,9),
   schedule=None, # use '0 6 * * *' to run the program at 6 am UTC everyday
   catchup=False
) as dag:
   subject = retrieve_subject()
   recipient_email = retrieve_recipient()
   attachment = retrieve_attachment()
   message = retrieve_message(attachment)
   
   send_email_task(recipient_email,subject,message,attachment)