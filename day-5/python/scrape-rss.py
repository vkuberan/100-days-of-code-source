import json
import requests
from bs4 import BeautifulSoup


def save_feed_to_json(chessfeed):
    with open('chessfeed.txt', 'w') as outfile:
        json.dump(chessfeed, outfile)


def chessmind_rss(rssurl="http://www.thechessmind.net/blog/rss.xml"):
    chess_news = []

    try:
        r = requests.get(rssurl)
        soup = BeautifulSoup(r.content, features='xml')

        chessnews = soup.findAll('item')

        for cn in chessnews:
            chess_news.append({
                'title': cn.find('title').text,
                'category': cn.find('category').text,
                'creator': cn.find('dc:creator').text,
                'publishedDate': cn.find('pubDate').text,
                'link': cn.find('link').text,
                'description': cn.find('description').text
            })

        return chess_news

    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


print('Starting scraping')

cf = chessmind_rss()

if cf != None:
    print("Feed information downloaded.")
    save_feed_to_json(cf)
    print("Saved to the file.")

print('Finished scraping')
