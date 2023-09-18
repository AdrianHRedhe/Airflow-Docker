from selenium import webdriver
from selenium.webdriver.common.by import By

# This function instansiates the remote driver. 
# Using the container name and the port 4444 both defined in
# the docker compose file, we can connect to the selenium 
# server started by docker.

def instantiateRemoteDriver():
    # This is the name of the container as defined in docker compose.
    remote_webdriver = 'remote_chromedriver'
    
    # Define that we want a chrome webdriver specifically.
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    
    # This is one of the most important flags.
    # The program will crash if the shm partition is too
    # small.
    options.add_argument('--disable-dev-shm-usage')

    # Using the container name, the right port and our chrome options we can
    # Insansiate and return the remote driver
    driver = webdriver.Remote(f'{remote_webdriver}:4444/wd/hub',options=options)

    return driver

# This is hardcoded to return the weather data from the site SMHI.
# In another example it might be better to leave things open ended
# But in this case I have a very explicit use case and will not
# showcase that.

def scrapeTables(driver):

    # Go to the website
    driver.get('https://www.smhi.se/vader/prognoser/ortsprognoser/q/Stockholm/2673730')

    # Find the pane where the individual days are located.
    root = driver.find_element(By.ID,'root')
    pane = root.find_elements(By.XPATH,'//*[@role="tabpanel"]')[0]

    # You need to click the buttons to be able to retrieve the weather data
    buttons = pane.find_elements(By.XPATH,'./Button')

    # Lets get the weather data for the rest of today and tomorrow by first clicking these days.
    buttons[0].click()
    buttons[1].click()

    # On the pane the weather data is now visible
    # and we can scrape the information.
    tables = pane.find_elements(By.XPATH,'./div/div/table/tbody')

    return tables