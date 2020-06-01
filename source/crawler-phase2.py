import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import lxml
import pandas as pd
import time
import copy

with open("./phase2-config.csv", newline='', encoding='utf-8-sig') as inputfile:
    reader = csv.reader(inputfile)
    filename1 = next(reader)[0] # phase 2 result
    filename2 = next(reader)[0] # final result

    
    with pd.ExcelWriter('./' + filename1 + '.xlsx', mode='w') as writer:
        with pd.ExcelWriter('./' + filename2 + '.xlsx', mode='w') as writer2:
            for [category, url] in reader:
                """ Built name-id dictionary for id searching """
                with open('source/name-id-'+ category +'.csv', newline='', encoding='utf-8-sig') as dict_file:
                    dict_reader = csv.reader(dict_file)
                    idDict = {student[1].strip():student[0] for student in dict_reader}

                """ Fetch page data from internet """
                options = webdriver.ChromeOptions()
                options.add_argument("headless") 
                options.add_argument("window-size=1920,1080") 
                driver = webdriver.Chrome("source/chromedriver", chrome_options=options)
                driver.get(url)
                time.sleep(6)
                soup = BeautifulSoup(driver.page_source, "lxml")
                # print(soup.prettify())

                """ Retrieve Candidate Info """
                data = []
                for link in soup.findAll("a"):
                    if("考區 : " in link.text): 
                        # Split candidate name and 考區
                        text = link.parent.text.replace('\n', '').replace(' ', '').split('考區:')
                        name = link.findNext("td", {"align" : "center"}).text.strip()
                        text[0] = idDict[name] # Search for id
                        text.append(name) 
                        # text = ['10000000', '臺北市立成功高中', '']
                        data.append(text)
                data_final = copy.deepcopy(data)

                """ Retrieve Departments Info """
                tables = soup.findAll("table") # Each table will become a row
                i = 0
                for table in tables[3:]:
                    for cell in table.findAll('td'):
                        for link in cell.findAll("a"):
                            if(link.text != "" and link.text != "\n"):
                                text = link.text
                                status = link.findNext("div", {"align" : "center"}).text
                                if status != "":
                                    text = text + '-' + status
                                data[i].append(text) # Add to each row

                    """ Fetch Final result """
                    text = "" 
                    for image in table.findAll("img"):
                        if "putdep1.png" in image['src']: # Look for the badge
                            final = image.findNext("a")
                            status = final.findNext("div", {"align" : "center"}).text
                            if status != "":
                                text = final.text + '-' + status
                            data_final[i].append(text)

                    i += 1 # Go to the next row

                """ Add header """
                data = [["准考證號", "考區", "考生姓名", "校系", "校系", "校系", "校系", "校系", "校系", "校系"]] + data
                data_final = [["准考證號", "考區", "考生姓名", "統一分發校系"]] + data_final

                """ Write to excel file """        
                df = pd.DataFrame(data)
                df.to_excel(writer, sheet_name=category, header=False, index=False)
                df2 = pd.DataFrame(data_final)
                df2.to_excel(writer2, sheet_name=category, header=False, index=False)
                driver.close()

print("Success")

