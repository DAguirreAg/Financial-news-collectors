from config import Config
import bbc_news.webpage_collector
import bbc_news.webpage_etl
import bloomberg_news.webpage_collector
import bloomberg_news.webpage_etl

if __name__ == '__main__':

    # Download BBC news
    config = Config()
    urls = config.NEWS_SETTINGS['BBC']['URLS']
    domain = config.NEWS_SETTINGS['BBC']['DOMAIN']
    download_path = config.NEWS_SETTINGS['BBC']['DOWNLOAD_PATH']
    bbc_news.webpage_collector.main(config, urls, domain, download_path)

    # ETL BBC news
    etl_consumption_path = config.NEWS_SETTINGS['BBC']['ETL_CONSUMPTION_PATH']
    bbc_news.webpage_etl.main(config, etl_consumption_path)

    # Download Bloomberg news
    config = Config()
    urls = config.NEWS_SETTINGS['Bloomberg']['URLS']
    domain = config.NEWS_SETTINGS['Bloomberg']['DOMAIN']
    download_path = config.NEWS_SETTINGS['Bloomberg']['DOWNLOAD_PATH']
    bloomberg_news.webpage_collector.main(config, urls, domain, download_path)
    
    # ETL Bloomberg news
    etl_consumption_path = config.NEWS_SETTINGS['Bloomberg']['ETL_CONSUMPTION_PATH']
    bloomberg_news.webpage_etl.main(config, etl_consumption_path)