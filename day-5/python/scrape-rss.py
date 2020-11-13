import requests
from bs4 import BeautifulSoup


def hackernews_rss('https://news.ycombinator.com/rss'):
    try:
        r = requests.get()
        return print('The scraping job succeeded: ', r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


print('Starting scraping')
hackernews_rss()
print('Finished scraping')
