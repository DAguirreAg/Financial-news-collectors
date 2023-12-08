-- Create Finance Database
CREATE DATABASE db_finance_universe;

/*
-- Create tables
--- news table
CREATE TABLE news (
    url VARCHAR NOT NULL PRIMARY KEY,
    title VARCHAR NOT NULL,
    publish_date DATE NOT NULL,
    tickers TEXT[][],
    domain VARCHAR NOT NULL,
    ref_filename VARCHAR NOT NULL,
    sentiment_analysis_score FLOAT,
    countries TEXT[][]
);*/

-- Create tables
--- news table
CREATE TABLE news (
    url VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    publish_date VARCHAR,
    tickers TEXT[][],
    countries TEXT[][],
    ref_filename VARCHAR NOT NULL,
    news_outlet VARCHAR NOT NULL,
    downloaded_datetime VARCHAR NOT NULL
);
