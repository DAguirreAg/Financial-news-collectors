
from config import Config
import bbc_news.webpage_collector


if __name__ == '__main__':

    # Download BBC news
    config = Config()
    urls = config.NEWS_SETTINGS['Bloomberg']['URLS']
    domain = config.NEWS_SETTINGS['Bloomberg']['DOMAIN']
    bbc_news.webpage_collector.main(config, urls, domain)

