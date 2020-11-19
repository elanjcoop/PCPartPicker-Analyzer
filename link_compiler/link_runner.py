import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
  
#url of the page we want to scrape 
url_a = "https://pcpartpicker.com/builds/#X=0,550000&page="
url_b = "&sort=rating"

# initiating the webdriver. Parameter includes the path of the webdriver. 
driver = webdriver.Chrome('./chromedriver')
f = open("url_list.txt", "w")


page_counter = 1
url_counter = 1

while True:
    try:
        driver.get(url_a + str(page_counter) + url_b)
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all('a', class_ = "logGroup__target"):
            url = link.get('href')
            f.write(url + "\n")
            print(url_counter)
            url_counter += 1
        page_counter += 1
    except KeyboardInterrupt:
        break
f.close()
driver.close() # closing the webdriver 