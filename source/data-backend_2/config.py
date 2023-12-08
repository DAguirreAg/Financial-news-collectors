import datetime

class Config:
    
    # Selenium settings
    WEBDRIVER_BROWSER = 'selenium-api'# Options: 'chrome' OR 'selenium-api'
    WAIT_PAUSE_TIME = 5 #seconds
    IMPLICIT_WAIT_TIME = 10 #seconds
    
    # News settings
    NEWS_SETTINGS = {
        'BBC': {
            'NEWS_OUTLET': 'BBC',
            'URLS': [
                'https://www.bbc.com/news',
                'https://www.bbc.com/news/science-environment-56837908',
                'https://www.bbc.com/news/world',
                'https://www.bbc.com/news/business',
                'https://www.bbc.com/news/technology',
                'https://www.bbc.com/news/science_and_environment',
                'https://www.bbc.com/news/stories'
            ],
            'DOWNLOAD_PATH': 'downloads/bbc/',
            #'ETL_CONSUMPTION_PATH': 'downloads/BBC/'
        },
    }
    '''
        'Bloomberg': {
            'DOMAIN': 'Bloomberg',
            'URLS': [
                'https://www.bloomberg.com/markets',
                'https://www.bloomberg.com/economics',
                'https://www.bloomberg.com/economics/indicators',
                'https://www.bloomberg.com/economics/central-banks',
                'https://www.bloomberg.com/economics/jobs',
                'https://www.bloomberg.com/economics/trade',
                'https://www.bloomberg.com/economics/tax-and-spend',
                'https://www.bloomberg.com/economics/inflation-and-prices',
            ],
            'DOWNLOAD_PATH': 'downloads/bloomberg/',
            #'ETL_CONSUMPTION_PATH': 'downloads/Bloomberg/'
        },
    '''
    
    # SCHEMAS
    STAGING_SCHEMA = {
        'title': str,
        'url': str,
        'publish_date': datetime,
        'tickers': list,
        'countries': list,
        'news_outlet': str,
        'ref_filename': str,
        'downloaded_datetime': datetime
    }
    
    # DATABASE
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@some-postgres:5432/postgres'
    #SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@127.0.0.1:5432/db_finance_universe'

    
    