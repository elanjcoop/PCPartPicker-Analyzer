"""
Goes through file or highest-rated links and uses BS4
to add builds with completed prices to database
"""
import sys
# import parent directory
sys.path.append("../")
from beautiful_soup_cleaner import get_list
from component_evaluator import price_total, is_all_components_present, component_percentage_list
import sqlite3
from sqlite3 import IntegrityError
import time

def link_prefixer(raw_link):
    return "https://pcpartpicker.com" + raw_link

conn = sqlite3.connect('Build_Percentage_Breakdown.db')
c = conn.cursor()
url_file = open("url_list.txt", "r")
databased_file = open("databased_builds.txt", "r+")
database_file_checked = open("databased_builds_checked.txt", "r+")

# Turn all of our previously checked url's from .txt into an array
# Did this due to newline errors; try to refactor
database_file_checked_cropped = []
for link in database_file_checked:
    changed_link = link.strip("\n")
    database_file_checked_cropped.append(changed_link)



"""
# Initial table build
# had to change name "case" to tower due to SQL syntax lol
c.execute('''CREATE TABLE builds
             ([generated_id] INTEGER PRIMARY KEY,[url] TEXT, [total_cost] REAL, 
              [cpu] REAL, [gpu] REAl, [storage] REAl, [memory] REAL, 
              [motherboard] REAL, [tower] REAL, [power_supply] REAL, 
              UNIQUE(url))''')

"""

while True:
    try:
        for url in url_file:
            url = url.strip('\n')
            if url in database_file_checked_cropped:
                continue
            else:
                time.sleep(3)
                html_link = link_prefixer(url)
                prices_per_component = get_list(html_link)
                total_price = price_total(prices_per_component)
                percentage_list = component_percentage_list(prices_per_component, total_price)
                database_file_checked.write(url + "\n")
                
                if is_all_components_present(prices_per_component):
                    try:
                        c.execute("INSERT INTO builds(url, total_cost, cpu, motherboard, memory, storage, gpu, tower, power_supply)" +
                              "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                              (html_link, total_price, percentage_list[0], percentage_list[1], percentage_list[2], 
                               percentage_list[3], percentage_list[4], percentage_list[5], percentage_list[6]))
                        databased_file.write(url + "\n")
                    except IntegrityError:
                        continue
    except KeyboardInterrupt:
        break

url_file.close()
databased_file.close()
database_file_checked.close()
conn.commit()