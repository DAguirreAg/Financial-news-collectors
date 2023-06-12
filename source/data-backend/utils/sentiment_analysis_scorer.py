import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append("..")
from config import Config
from models import news

# Instantiate the sentiment intensity analyzer
vader = SentimentIntensityAnalyzer()

def get_sentiment_analysis_score(title):

    if title is None:
        return 0

    # Calculate the sentiment score
    vader_scores = vader.polarity_scores(title)
    score = vader_scores['compound']

    return score

def update_news_sentiment_analysis(config):

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
        score = get_sentiment_analysis_score(title)
        
        # Update value
        session.query(news).where(news.c.url == url).update({news.c.sentiment_analysis_score: score})
        session.commit()

if __name__ == '__main__':

    config = Config()

    update_news_sentiment_analysis(config)