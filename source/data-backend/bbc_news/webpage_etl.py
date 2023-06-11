import sys
sys.path.append("..")

from bs4 import BeautifulSoup
import datetime
import json
from config import Config
import glob
import utils.sql_utils as sql_utils

# Helper functions
def get_title(headline):
        
    # Title
    try:
        title = headline.find("a", {"class": "nw-o-link-split__anchor"}).text
    
    except:
        title = None
        
    finally:
        if title:
            title = title.strip()
    
    return title

def get_url(headline):
    
    # Url
    try:        
        href = headline.find("a", {"class": "nw-o-link-split__anchor"})['href']

    except:
        href = None
        
    finally:
        if href:
            url = 'https://www.bbc.com' + href
        else:
            url = href
    
    return url

def get_publish_date(headline):
    
    # Publish date
    publish_date = None
    
    try:
        
        # Get publish datetime
        datetime_str = headline.find('time', {'class': 'date'})['datetime']
        
        # Get publish date
        date_str = datetime_str.split('T')[0]

        # Convert to datetime
        publish_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    except IndexError as e:
        #print(e)
        pass
    
    except ValueError as e:
        #print(e)
        pass
    
    except TypeError as e:
        #print(e)
        pass

    return publish_date

def get_tickers(headline):
    
    # Tickers
    tickers = []

    return tickers

def extract_headline_data(headline):
    
    # Extract data
    extract = {    
        'title': get_title(headline),
        'url': get_url(headline),
        'publish_date': get_publish_date(headline),
        'tickers': get_tickers(headline) 
    }
    
    return extract

def get_headlines(soup):
    # Get headlines
    headlines = soup.find_all('div', {'class': 'gel-layout__item'})

    # Extract info from headlines
    news = []
    for headline in headlines:
        extract = extract_headline_data(headline)

        # Validate extracted data
        is_valid = validate_extract(extract)

        if is_valid:
            news.append(extract)

    return news

def validate_extract(extract):
    
    title = extract['title']
    url = extract['url']
    publish_date = extract['publish_date']
    
    if title is None or title == '':
        return False
    
    if url is None or url == '':
        return False
    
    if publish_date is None or publish_date == '':
        return False

    return True

def main(config, etl_consumption_path):

    load_from = config.RAW_FORMAT
    
    if load_from == 'file':
        
        # Get available files
        filename_paths = glob.glob(etl_consumption_path + "*.json")

        for filename_path in filename_paths:
            print(f'ETL: {filename_path}')

            # Load file
            with open(filename_path, 'r') as j:
                webpage = json.loads(j.read())

            # Extract
            html = webpage['html']
            soup = BeautifulSoup(html, 'html.parser')

            # Get headlines
            news = get_headlines(soup)

            # Add domain and ref_filename info
            domain = webpage['domain']
            ref_filename = filename_path.split('/')[-1]
            for news_item in news:
                news_item['domain'] = domain
                news_item['ref_filename'] = ref_filename

            # Insert news
            sql_utils.insert_data_into_db_news_table(news)
        
    elif load_from == 'mongoDB':
        # TO DO
        pass
    
    else:
        raise Exception(f'"load_from" parameter received unexpected value. Please revise.')

if __name__ == '__main__':

    config = Config()
    etl_consumption_path = config.NEWS_SETTINGS['BBC']['ETL_CONSUMPTION_PATH']
    main(config, etl_consumption_path)


