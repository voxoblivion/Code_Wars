import requests
from bs4 import BeautifulSoup
import operator

def getWords(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,'html.parser')
    for title in soup.findAll('div', {'class ': 'tile__name'}):
        content = (title.string + ' test')
        print(content)
    return soup.findAll('div', {'class':'tile__name'})

print(getWords('https://www.g2a.com/en/best-offers/weeklysale?banner=main&shop=global'))
