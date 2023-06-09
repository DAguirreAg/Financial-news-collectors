import pymongo
import datetime
from config import Config

# Create connections
mongodb_client = pymongo.MongoClient(Config.MONGODB_DATABASE_URL)
mongodb = mongodb_client["financial_news"]

# Create the collections
webpage_collection = mongodb["webpages"]

def add_webpage(url: str, domain: str, html: str):
    
    # Create the webpage dict
    webpage = {
            'url': url,
            'domain': domain,
            'extracted_time': str(datetime.datetime.now()),
            'html': html
    }
    
    # Insert webpage
    webpage_collection.insert_one(webpage)