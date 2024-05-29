#test de beautifulsoup4 lib de scraping

import bs4 as bs
#import urllib.request
import requests

#source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
html = requests.get("https://pythonprogramming.net/parsememcparseface/")


soup = bs.BeautifulSoup(html.text, 'lxml')

for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

for url in soup.find_all('a'):
    print(url.get('href'))