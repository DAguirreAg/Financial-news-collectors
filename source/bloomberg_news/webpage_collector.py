import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from config import Config
from utils import add_webpage

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    
    # Start driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.implicitly_wait(Config.WAIT_PAUSE_TIME) # seconds to wait
    
    try:
        # Get request from URL
        for url in Config.URLS:

            # Go to url
            try:
                driver.get(url)

                # Wait to load page
                time.sleep(Config.WAIT_PAUSE_TIME)

            except WebDriverException as e:
                # To DO: Add logging of errors
                continue

            # Save HTML to Database
            html_doc = driver.page_source
            add_webpage(url, Config.DOMAIN, html_doc)
            
    except Exception as e:
        # To DO: Add logging of errors
        raise Exception(e)
    
    finally:
        
        # Close driver
        driver.close()