from selenium import webdriver

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