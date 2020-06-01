import requests
from bs4 import BeautifulSoup
import csv
import lxml
import pandas as pd

with open("./phase1-config.csv", newline='', encoding='utf-8-sig') as inputfile:
    reader = csv.reader(inputfile)
    filename = next(reader)[0]
    with pd.ExcelWriter('./' + filename + '.xlsx', mode='w') as writer:
        for [category, link] in reader:

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
                            text = link.text
                            date = link.findNext("div", class_='retestdate').text.replace(' ', '')
                            if date[0] != '-':
                                text = link.text + '-' + date
                            data[i].append(text) # Add to each row
                i += 1 # Go to the next row

            """ Add header """
            data = [["准考證號", "考區", "考生姓名", "校系", "校系", "校系", "校系", "校系", "校系", "校系"]] + data

            """ Write to excel file """
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=category, header=False, index=False)

