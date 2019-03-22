import urllib3
from bs4 import BeautifulSoup

url = 'http://alterportal.ru'

http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")
print(soup)