from bs4 import BeautifulSoup
import json
import requests

page = requests.get('https://www.tps.uz/articles/view/tendery')
soup = BeautifulSoup(page.text, 'html.parser')

div = soup.find(class_='content')

titleList = div.find('table')
td = len(titleList.find_all('td'))

titleList = list(titleList)



js_body = {
    'tps_tenders' : {}
}

def normalize(value):
  value = value.text
  value = value.replace('\r', '')
  value = value.replace('\n', '')
  value = value.replace('\t', '')
  value = value.split('   ')
  return value

keyCounter = 0
valueCounter = 1


for i in range(0, td):

        js_body = {
            'title': normalize(div.find_all('td')[keyCounter]),
            'body': normalize(div.find_all('td')[valueCounter]),
        }

        keyCounter += 2
        valueCounter += 2

        jsb = json.dumps(js_body)
        print(json.loads(jsb))
