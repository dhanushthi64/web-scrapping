import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from shutil import copyfileobj


# Specify the URL of the webpage
url = "https://sightwords.com"

# Make a GET request to fetch the HTML content of the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the image tags from the webpage
img_tags = soup.find_all('img')

# Extract the source URLs of all the images and download them
for img in img_tags:
    img_url = img['src']
    filename = img_url.split("/")[-1]
    with urlopen(img_url) as inf, open('filename','wb') as outf:
        copyfileobj(inf,outf)    

