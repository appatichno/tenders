from bs4 import BeautifulSoup
from itertools import zip_longest
import json
import requests


def bigrams(tokens):
    for t in zip_longest(tokens[:],tokens[1:],fillvalue=''):
        yield ''.join(t)

def creteFullLink(link):
    urlA = ['https://corp.uzairways.com']
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

url="https://corp.uzairways.com/ru/press-center/tenders?page=0"

main_page = requests.get(url)
soup = BeautifulSoup(main_page.text, 'html.parser')
count = len(soup.find_all(class_= "articles__title"))
js_body = []
for link in soup.find_all(class_ = "articles__title" ):
    link=creteFullLink(link.get('href'))
    for link_text in range(1):
        link_page = requests.get(link)
        link_soup = BeautifulSoup(link_page.text, 'html.parser')
        link_soup = link_soup.find(class_='news-description-container')
        link_title = link_soup.find('h2')
        link_text = link_soup.find('div')
        link_link = link_soup.find(class_='download__link')
        js_body= {
            'title': normalize(link_title),
            'body': normalize(link_text),
            'link': creteFullLink(link_link.get('href')),
        }
        jsb = json.dumps(js_body)
        print(json.loads(jsb))



