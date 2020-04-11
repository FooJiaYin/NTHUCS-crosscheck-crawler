import requests
from bs4 import BeautifulSoup
import csv
import lxml

""" Input link and filename """
category = input("Category: ")
link = input("Link: ")

""" Fetch data from internet """
res = requests.get(link)
soup = BeautifulSoup(res.text, "lxml")
# print (soup.prettify())

""" Retrieve Candidate Info """
data = []
for link in soup.findAll("a"):
    if("考區 : " in link.text): 
        # Split candidate id and 考區
        text = link.parent.text.replace('\n', '').replace(' ', '').split('考區:')
        text.append('') 
        # text = ['10000000', '臺北市立成功高中', '']
        data.append(text)

""" Retrieve Departments Info """
tables = soup.findAll("table") # Each table will become a row
i = 0
for table in tables[3:]:
    for cell in table.findAll('td'):
        for link in cell.findAll("a"):
            if(link.text != "" and link.text != "\n"):
                data[i].append(link.text) # Add to each row
    i += 1 # Go to the next row

""" Add header """
data = [["准考證號", "考區", "考生姓名", "校系", "校系", "校系", "校系", "校系", "校系", "校系"]] + data

""" Write to csv file """
with open(category + ".csv", "w", newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile, dialect='excel')
    writer.writerows(data)
