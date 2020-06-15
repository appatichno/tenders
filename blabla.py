from bs4 import BeautifulSoup
from itertools import zip_longest
import json
import requests


def bigrams(tokens):
    for t in zip_longest(tokens[:], tokens[1:], fillvalue=''):
        yield ''.join(t)


url = "https://corp.uzairways.com/ru/press-center/tenders?page=0"
urlA = ['https://corp.uzairways.com']
main_page = requests.get(url)
soup = BeautifulSoup(main_page.text, 'html.parser')

for link in soup.find_all(class_="articles__title"):
    a = link.get('href')
    a = a.split('  ')
    a = list(a)
    a = urlA + a
    a = list(bigrams(a))
    a = a[0]

    tpage = requests.get(a)
    tsoup = BeautifulSoup(tpage.text, 'html.parser')
    for div in tsoup.find_all(class_="news-description-container"):
        # text = div.find_all('h2'(')
        # title = div.find_all()
        print(div.text)


