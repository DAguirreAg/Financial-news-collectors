from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from config import Config
import pandas as pd

# Create connections
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)

def insert_data_into_db_news_table(news: dict):

    dff = pd.DataFrame(news)
    
    # Connect to DB and insert data
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
    
    # Insert items one at a time to handle uniqueness complains
    for i in range(len(dff)):
        try:
            dff.iloc[i:i+1].to_sql("news", con=engine, if_exists='append', index=False)
        except IntegrityError:
            pass
