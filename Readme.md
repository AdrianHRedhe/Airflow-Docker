# Airflow simple scrape

Scheduled scrape that is run through airflow and docker, it sends an email with  
the scraped information in a CSV file to a recipient of your choosing. 

The actual problem of collecting weatherdata is not really one that requires this  
complex setup. However, a scheduled scrape that sends the information in an email  
is something that I have wanted to have, to solve other problems in my daily life.

It works using docker to run both an Airflow server and a Selenium server, using a  
remote webdriver to run the scrape via the selenium server. This is my first time  
working with Airflow to try to understand how it works and what I can do with it. 

## Authors

- [@AdrianHRedhe](https://www.github.com/adrianhredhe)

## Environment Variable

Due to running the project in docker and using a .env file being a bit cumbersome just  
for one variable it was decided this project would not to use a .env file

Instead you can navigate to `/dags/scrapeAndEmailDag.py` or click [here](/dags/scrapeAndEmailDag.py) and change  
the variable `RECIPIENT_EMAIL` in the function `retrieveRecipient()` to the email  
you want to send the scraping results to, i.e. `RECIPIENT_EMAIL = 'name@gmail.com'`

## Required

To run the program you do will need to install [docker](https://docs.docker.com/get-docker/) on your machine

## Run Locally

Clone the project

```bash
  git clone https://github.com/AdrianHRedhe/Airflow-Docker.git
```

Go to the project directory

```bash
  cd Airflow-Docker
```

Run the docker container

```bash
  docker compose up
```

Go to [localhost:8080](http://localhost:8080/) on your browser.

Log in using the following username & password: 
* Username: `airflow`
* Password: `airflow`

Click on the `Scrape_And_Email_Me_Info` DAG. In the top-right corner there is a play button (`▶️`)  
click on it and then click on `Trigger DAG`

You should now have recieved an email with a scraped file as long as you defined your email  
correctly in /dags

You can also go to the page [SMHI](https://www.smhi.se/vader/prognoser/ortsprognoser/q/Stockholm/2673730) to look and make sure that the scraping has in-fact collected  
the correct information