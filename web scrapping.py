import requests
from bs4 import BeautifulSoup
url = 'https://www.tvcnews.tv/politics/'
response = requests.get(url)
# print(response)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify)

for news in soup.find_all('article'):
    title = news.find('h3').text.strip()
    print(title)
    img = news.find('img')
    print(img)