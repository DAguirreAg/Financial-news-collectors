
class Config:

    # DB settings
    ## MONGODB
    MONGODB_DATABASE_URL = 'mongodb://localhost:27017/'

    ## POSTGRESQL
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/db_finance_universe'

    # Directory settings
    DOWNLOAD_PATH = 'downloads'
    FILENAME_PREFIX = 'Output_'

    ETL_CONSUMPTION_PATH = 'downloads/'
    
    # Selenium settings
    CHROMEDRIVER_PATH = 'chromedriver_linux64/chromedriver'
    HEADLESS = False
    WAIT_PAUSE_TIME = 3 #seconds
    SCROLL_PAUSE_TIME = 2 #seconds
    
    # Bloomberg news settings
    DOMAIN = 'Bloomberg'

    URLS = [
        #'https://www.bloomberg.com/markets',
        'https://www.bloomberg.com/economics',
        #'https://www.bloomberg.com/economics/indicators',
        #'https://www.bloomberg.com/economics/central-banks',
        #'https://www.bloomberg.com/economics/jobs',
        #'https://www.bloomberg.com/economics/trade',
        #'https://www.bloomberg.com/economics/tax-and-spend',
        #'https://www.bloomberg.com/economics/inflation-and-prices'     
        ]
    
    # How the collected files will be saved/loaded: Folder/File or MongoDB
    RAW_FORMAT = 'file'

