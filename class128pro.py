from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" 
browser = webdriver.Chrome("C:/Users/drbis/Downloads/chromedriver_win32/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers=["Proper name","Distance","Mass","Radius","Luminosity"]
star_data=[]
final_star_data=[]
def scrape():
    
    for i in range(0,522):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs={"class","brightestStar"}):
            th_tags=tr_tag.find_all("th")
            temp_list=[]
            for index,th_tag in enumerate(th_tags):
                if index==0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")

            hyperlink_th_tag=th_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")  
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
def scrape_more_data(hyperlink):
        page = requests.get(hyperlink)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("ul",attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
            temp_list=[]
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")   
scrape() 

for data in star_data:
    scrape_more_data(data[5])

final_planet_data=[]

for index,data in enumerate(star_data):
    final_star_data.append(data+final_star_data[index])

with open("final2.csv","w",encoding="utf-8") as f:
        csvwriter = csv.writer(f)                  
        csvwriter.writerow(headers)
        csvwriter.writerow(final_star_data)
                         