import sys
sys.path.append("..")

import time
from config import Config
import utils.save_utils as mongodb_utils

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import random

def main(config: Config, urls: str, domain: str, download_path: str):

    # Driver settings
    chrome_options = Options()
    if config.HEADLESS == True:
        chrome_options.add_argument("--headless")

    # Start driver
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options) 
    driver.implicitly_wait(config.WAIT_PAUSE_TIME) # seconds to wait
    
    try:
        # Get request from URL
        for url in urls:
            print(f'Downloading: {url}')

            # Go to url
            try:
                driver.get(url)

                # Wait to load page
                time.sleep(config.WAIT_PAUSE_TIME + random.random()*5 )

            except WebDriverException as e:
                # To DO: Add logging of errors
                continue

            # Save HTML
            html_doc = driver.page_source
            mongodb_utils.save_webpage(config, url, domain, html_doc, config.RAW_FORMAT, download_path)
            
    except Exception as e:
        # To DO: Add logging of errors
        raise Exception(e)
    
    finally:
        
        # Close driver
        driver.close()
        
if __name__ == '__main__':
    
    config = Config()
    urls = config.NEWS_SETTINGS['BBC']['URLS']
    domain = config.NEWS_SETTINGS['BBC']['DOMAIN']
    download_path = config.NEWS_SETTINGS['BBC']['DOWNLOAD_PATH']
    
    main(config, urls, domain, download_path)