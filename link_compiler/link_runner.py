import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
 
url_a = "https://pcpartpicker.com/builds/#X=0,550000&page="
url_b = "&sort=rating"

#driver = webdriver.Chrome('./chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("disable-infobars");
chrome = webdriver.Chrome('./chromedriver', options=chrome_options)
chrome.delete_all_cookies()
# do around 1000 at a time, so make n increase (url_list_n.txt)
f = open("url_list_4.txt", "w")

# page count represents current iteration, usually do
# around 50 per run, then evaluate (50 * 20) (page * links/page) links
page_counter = 225
url_counter = 1

while True:
    try:
        chrome.get(url_a + str(page_counter) + url_b)
        time.sleep(10)
        html = chrome.page_source
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