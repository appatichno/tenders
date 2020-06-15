from bs4 import BeautifulSoup
from itertools import zip_longest
import json
import requests
from fake_useragent import UserAgent
import time
UserAgent().chrome


def bigrams(tokens):
    for t in zip_longest(tokens[:],tokens[1:],fillvalue=''):
        yield ''.join(t)

def creteFullLink(link):
    urlA = ['https://company.mobi.uz']
    link = link.split('  ')
    link = list(link)
    link = urlA + link
    link = list(bigrams(link))
    link = link[0]
    return link

def normalize(value):
  value = value.text
  value = value.replace('\r', '')
  value = value.replace('\n', '')
  value = value.replace('\t', '')
  value = value.replace('\xa0', '')
  value = value.split('   ')
  return value


result = {
    'list' : {}
}
url="https://company.mobi.uz/ru/purchase/"

main_page = requests.get(url, headers={'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
soup = BeautifulSoup(main_page.text, 'html.parser')
div = soup.find('div',{"class":"news-list"})
count = len(div.find_all('a',{"class":"news-item__link"}))
js_body = []

for link in div.find_all('a',{"class":"news-item__link"}):

    time.sleep(0.1)

    link=creteFullLink(link.get('href'))

    for link_text in range(1):
        link_page = requests.get(link)

        link_soup = BeautifulSoup(link_page.text, 'html.parser')
        link_soup = link_soup.find('div',{"class":"main-content"})
        text= link_soup.text
        link_title = link_soup.find('h1')
        link_text = link_soup.find(class_="inner-content")
        link_link = link_soup.find('a')
        js_body = {
            'title': normalize(link_title),
            'body': normalize(link_text),
            'link': creteFullLink(link_link.get('href')),
        }
        jsb = json.dumps(js_body)
        print(json.loads(jsb))
