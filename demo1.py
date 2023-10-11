from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.jstage.jst.go.jp/browse/mej/list/-char/en')
soup = BeautifulSoup (response.text,'lxml')
print(soup)

for page in soup.find_all('a',class_='bluelink-style customTooltip'):
    href = page['href']
    print(href)

