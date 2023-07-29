import requests
import bs4
res= requests.get('https://sightwords.com')
print(res.text)
soup=bs4.BeautifulSoup(res.text,'html.parser')
for link in soup.find_all('a',href=True):
    if link['href'].startswith("http"):
        print(link['href'])