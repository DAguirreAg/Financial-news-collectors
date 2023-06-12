from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, ARRAY

meta = MetaData()

news = Table(
   'news', meta, 
   Column('url', String, nullable = False, primary_key = True), 
   Column('title', String, nullable = False), 
   Column('publish_date', Date, nullable = False), 
   Column('tickers', String), 
   Column('domain', String, nullable = False), 
   Column('ref_filename', String, nullable = False), 
   Column('sentiment_analysis_score', Float),
   Column('countries', ARRAY(String)),

)