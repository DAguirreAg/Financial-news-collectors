import os

class Config:
    
    # DB settings
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/db_finance_universe'

    # App settings
    ## Metadata 
    DESCRIPTION = '''
    Dashboard to display the collected news.
    '''

    TAGS_METADATA = [
        {
            "name": "News",
            "description": "Operations with the news.",
        }
    ]

    TITLE="Financial news collector App"
    VERSION="0.0.1"
    CONTACT={
            "name": "DAguirreAg",
            "url": "https://github.com/DAguirreAg/"
            }
    LICENSE_INFO={
                "name": " MIT License",
                "url": "https://mit-license.org/",
                }