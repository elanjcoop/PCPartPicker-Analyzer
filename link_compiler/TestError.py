from bs4 import BeautifulSoup
import requests

#source = requests.get("http://pcpartpicker.com/b/sPYJ7P")
source = requests.get("https://pcpartpicker.com/b/HKRkcf")
soup = BeautifulSoup(source.text, 'lxml')
print("+" + soup.find(class_="block markdown").string.strip("\n") + "+")
print(source.status_code)