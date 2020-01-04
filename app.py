import requests
from bs4 import BeautifulSoup
import json
import pprint
import sys
import settings
from emails import send_email

exclusion_list = ['http://www.nytimes.com/services/mobile/index.html', 'https://www.nytimes.com/subscription/cooking.html']
url = "https://nytimes.com"

webpage = requests.get(url)
page_contents = BeautifulSoup(webpage.content, 'lxml')

articles = page_contents.find_all('a')
if not articles:
    print("Nothing found")
    sys.exit()

front_page_articles = []

for article in articles:
    if '.html' in article.attrs['href'] and article.attrs['href'] not in exclusion_list:
        if "https://www.nytimes.com" not in article.attrs['href']:
            front_page_articles.append('https://www.nytimes.com' + article.attrs['href'])
        else:
            front_page_articles.append(article.attrs['href'])

pprint.pprint(set(front_page_articles), indent=2)

send_email()