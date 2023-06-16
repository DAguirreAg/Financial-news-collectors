import pymongo
import datetime
from config import Config
import json
import os

# Create connections
mongodb_client = pymongo.MongoClient(Config.MONGODB_DATABASE_URL)
mongodb = mongodb_client["financial_news"]
webpage_collection = mongodb["webpages"] # Create the collections

def save_webpage_mongoDB(webpage):
    # Insert webpage
    webpage_collection.insert_one(webpage)

def save_webpage_local_storage(config, download_path, webpage):
    # Convert into JSON:
    webpage_json = json.dumps(webpage)
        
    # Create filename
    filename_datetime = str(datetime.datetime.now()).replace(' ', '_').replace('-', '').replace(':', '').split('.')[0]
    filename = config.FILENAME_PREFIX + filename_datetime + '.json'
    filename = os.path.join(download_path, filename)

    # Check if the directory exists
    if not os.path.exists(download_path):
        # If it doesn't exist, create it
        os.makedirs(download_path)

    # Save to a new file
    with open(filename, "w") as text_file:
        text_file.write(webpage_json)

def save_webpage_googleDrive(webpage):
    # TO DO
    pass

def save_webpage(config: Config, url: str, domain: str, html: str, save_to: str, download_path: str = None):
        
    # Create the webpage dict
    webpage = {
            'url': url,
            'domain': domain,
            'extracted_time': str(datetime.datetime.now()),
            'html': html
    }
    
    if save_to == 'file':
        save_webpage_local_storage(config, download_path, webpage)
                
    elif save_to == 'mongoDB':
        save_webpage_mongoDB(webpage)

    elif save_to == 'googleDrive':
        save_webpage_googleDrive(webpage)

    else:
        raise Exception(f'"save_to" parameter received unexpected value: {save_to}. Please revise.')