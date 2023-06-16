
class Config:

    # DB settings
    ## MONGODB
    MONGODB_DATABASE_URL = 'mongodb://localhost:27017/'

    ## POSTGRESQL
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/db_finance_universe'

    # Directory settings
    FILENAME_PREFIX = 'Output_'
    
    # Selenium settings
    CHROMEDRIVER_PATH = 'chromedriver_linux64/chromedriver'
    HEADLESS = False
    WAIT_PAUSE_TIME = 3 #seconds
    SCROLL_PAUSE_TIME = 2 #seconds
    RAW_FORMAT = 'mongoDB' # How the collected files will be saved/loaded: Folder/File or MongoDB

    # Bloomberg news settings
    NEWS_SETTINGS = {
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
            'DOWNLOAD_PATH': 'downloads/Bloomberg/',
            'ETL_CONSUMPTION_PATH': 'downloads/Bloomberg/'
        },
        'BBC': {
            'DOMAIN': 'BBC',
            'URLS': [
                'https://www.bbc.com/news',
                'https://www.bbc.com/news/science-environment-56837908',
                'https://www.bbc.com/news/world',
                'https://www.bbc.com/news/business',
                'https://www.bbc.com/news/technology',
                'https://www.bbc.com/news/science_and_environment',
                'https://www.bbc.com/news/stories'
            ],
            'DOWNLOAD_PATH': 'downloads/BBC/',
            'ETL_CONSUMPTION_PATH': 'downloads/BBC/'
        },
    }

