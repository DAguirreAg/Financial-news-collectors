import sys
sys.path.append("..")

from bs4 import BeautifulSoup
import datetime
import json
from config import Config
import glob
import utils.sql_utils as sql_utils
import utils.sentiment_analysis_scorer as sentiment_analysis_scorer

# Helper functions
def get_title(headline):
    
    # Title
    title = headline.text
    
    if title:
        title = title.strip()
    
    return title

def get_url(headline):
    
    # Url
    href = headline.find('a')['href']
    if href:
        url = 'https://www.bloomberg.com' + href
    else:
        url = href
        
    return url

def get_publish_date(headline):
    
    # Publish date
    publish_date = None
    
    try:
        # Url
        href = headline.find('a')['href']
    
        # Get publish date
        date_str = href.split('/')[3]

        # Convert to datetime
        publish_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    except IndexError as e:
        #print(e)
        pass
    
    except ValueError as e:
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
        'tickers': get_tickers(headline),
        'sentiment_analysis_score': sentiment_analysis_scorer.get_sentiment_analysis_score(get_title(headline))
    }
    
    return extract

def get_headlines(soup):
    # Get headlines
    headlines = soup.find_all("div", attrs={"data-component": "headline"})

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
    etl_consumption_path = config.NEWS_SETTINGS['Bloomberg']['ETL_CONSUMPTION_PATH']
    main(config, etl_consumption_path)