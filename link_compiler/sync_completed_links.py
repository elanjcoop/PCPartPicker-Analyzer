"""
Add completed url's from database to text file "databased_builds"
"""

import sqlite3

file = open("databased_builds.txt", "w")
file.truncate(0)

conn = sqlite3.connect('Build_Percentage_Breakdown.db')
c = conn.cursor()

c.execute("SELECT url FROM builds")

rows = c.fetchall()

for row in rows:
    link = row[0]
    link = link.replace("https://pcpartpicker.com", "")
    file.write(link + "\n")

file.close()