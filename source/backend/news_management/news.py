from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from dependencies import get_db

router = APIRouter(
    #prefix="/",
    tags=["News"],
    responses={404: {"description": "Not found"}}
)

@router.get('/news_amount')
def get_news_amount(db: Session = Depends(get_db)):

    sql_statement = text("SELECT COUNT(1) AS count FROM news;")
    results = db.execute(sql_statement)
    amount = results.mappings().all()

    return amount[0]

@router.get('/source_amount')
def get_source_amount(db: Session = Depends(get_db)):

    sql_statement = text("SELECT COUNT(DISTINCT(domain)) AS count FROM news;")
    results = db.execute(sql_statement)
    amount = results.mappings().all()

    return amount[0]

@router.get('/country_amount')
def get_country_amount(db: Session = Depends(get_db)):

    sql_statement = text('''
    WITH cte_distinct_countries AS (
        SELECT
            DISTINCT(UNNEST(countries))
        FROM news
    )

    SELECT 
        COUNT(1)
    FROM cte_distinct_countries;
    ''')
    results = db.execute(sql_statement)
    amount = results.mappings().all()

    return amount[0]

@router.get('/recent_news')
def get_recent_news(db: Session = Depends(get_db)):

    sql_statement = text('''
    WITH cte_max_date AS (
        SELECT 
            MAX(publish_date)
        FROM news
    )

    SELECT 
        publish_date,
        title,
        sentiment_analysis_score
    FROM news
    WHERE publish_date = (SELECT * FROM cte_max_date)
    LIMIT 10;
    ''')
    results = db.execute(sql_statement)

    return results.mappings().all()

@router.get('/news_amount_over_time')
def get_news_amount_over_time(db: Session = Depends(get_db)):

    sql_statement = text('''
    SELECT
        publish_date,
        COUNT(1) AS count
    FROM news
    GROUP BY publish_date
    ORDER BY publish_date;
    ''')
    results = db.execute(sql_statement)
    
    return results.mappings().all()