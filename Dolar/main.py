import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
altin = soup.find("div", {"class": "market-data"}).find_all("span")[1].text
dolar = soup.find("div", {"class": "market-data"}).find_all("span")[4].text
euro = soup.find("div", {"class": "market-data"}).find_all("span")[7].text

print(f'Anlık altın kur: {altin} tl')
print(f'Anlık dolar kur: {dolar} tl')
print(f'Anlık euro kur: {euro} tl')
