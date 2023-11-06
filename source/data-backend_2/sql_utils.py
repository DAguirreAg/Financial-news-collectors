from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from config import Config
import pandas as pd

# Create connections
engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def insert_data_into_db_news_table(news: dict):

    dff = pd.DataFrame(news)
        
    # Insert items one at a time to handle uniqueness complains
    for i in range(len(dff)):
        try:
            dff.iloc[i:i+1].to_sql("news", con=engine, if_exists='append', index=False)
        except IntegrityError:
            pass

def get_distinct_ref_filenames():

    sql_statement = text('''
    SELECT
        DISTINCT(ref_filename)
    FROM news;
    ''')
    results = db.execute(sql_statement)
    
    distinct_urls = []
    for url in results.mappings().all():
        distinct_urls.append(url['ref_filename'])
        
    return distinct_urls