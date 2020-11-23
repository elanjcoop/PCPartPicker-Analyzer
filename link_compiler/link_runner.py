import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
 
url_a = "https://pcpartpicker.com/builds/#X=0,550000&page="
url_b = "&sort=rating"

driver = webdriver.Chrome('./chromedriver')
# do around 1000 at a time, so make n increase (url_list_n.txt)
f = open("url_list.txt", "w")

# page count represents current iteration, usually do
# around 50 per run, then evaluate (50 * 20) (page * links/page) links
page_counter = 51
url_counter = 1

while True:
    try:
        driver.get(url_a + str(page_counter) + url_b)
        time.sleep(15)
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