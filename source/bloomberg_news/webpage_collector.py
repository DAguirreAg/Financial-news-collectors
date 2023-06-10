import sys
sys.path.append("..")

import time
from config import Config
import utils.mongodb_utils as mongodb_utils

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':

    # Start driver
    chrome_options = Options()
    if Config.HEADLESS == True:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options) 
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

            # Save HTML
            html_doc = driver.page_source
            mongodb_utils.add_webpage(url, Config.DOMAIN, html_doc, Config.RAW_FORMAT)
            
    except Exception as e:
        # To DO: Add logging of errors
        raise Exception(e)
    
    finally:
        
        # Close driver
        driver.close()