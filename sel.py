from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s=Service('C:\webdrivers')
driver=webdriver.Chrome(service=s)
driver.get("https://youtube.com/")
url=driver.find_element(by=By.LINK_TEXT, value="/html/body/main/div[2]/div/ul/li[15]/div/a")
print(url.get_attribute('href'))
