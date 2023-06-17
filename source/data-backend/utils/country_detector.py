import pycountry

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append("..")
from config import Config
from models import news

def get_countries(title: str):

    if title is None:
        return 0

    # Get countries mentioned
    countries = []
    for country in pycountry.countries:
        if country.name in title:
            countries.append(country.name)

    return countries

def update_news_countries(config: Config):

    engine = create_engine(config.SQLALCHEMY_DATABASE_URL, echo = False)
    Session = sessionmaker(bind = engine)
    session = Session()

    # Get news
    rows = session.query(news).all()

    # Update the sentiment score for each row
    for row in rows:
        
        # Get url and title
        url = row[0]
        title = row[1]
        
        # Get the sentiment score
        countries = get_countries(title)
        
        # Update value
        session.query(news).where(news.c.url == url).update({news.c.countries: countries})
        session.commit()

if __name__ == '__main__':

    config = Config()

    update_news_countries(config)