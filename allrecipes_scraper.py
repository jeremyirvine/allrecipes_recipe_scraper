
import urllib
import requests
import urllib
import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from os.path  import basename

# Global Variables
final = []
# ================

browser = webdriver.Chrome("D:\Program Files\chromedriver_win32\chromedriver.exe")

browser.get("https://allrecipes.com/recipes")

elem = browser.find_element_by_tag_name("body")

page_start = 250

page_end = 200

page_rec_density = 20

iteration = 0

href_arr = []

last_density = 0;

while (page_start > 0 and page_start != page_end):
    
    browser.get("https://allrecipes.com/recipes/?page=" + str(page_start))
    last_url = ""
    hrefs = browser.find_elements_by_xpath("//a[contains(@href,'/recipe/')]")
    counter = 0
    for sr02 in hrefs:
        if(last_url != sr02.get_attribute("href")):
            href_arr.append(sr02.get_attribute("href"))
            counter+=1
        last_url = sr02.get_attribute("href")
    print("Processing " + str(counter) + " recipes...")
    counter2 = 0;
    for url in href_arr:
    
            
        print("Starting " + str(counter2 + (last_density * iteration)) + "/" + str(counter) + "(" + url + ")...")
        resp = urllib.urlopen(url) # open url
        html_doc = resp.read()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_doc, 'lxml')
        rec_title = soup.find(class_="recipe-summary__h1").text

        # print("rec_title: " + rec_title)

        ing = soup.findAll(class_="recipe-ingred_txt added")
        arr = []
        arr2 = []

        for link in ing:
            arr.append(link.text)

        for link2 in arr:
             arr2.append(link2.replace(" ", "|") + " ")

        rec_ing = ''.join(arr2)

        # print("\nrec_ing: '" + rec_ing + "'")


        tmp = soup.findAll(class_="step")
        rec_proc = []

        for link3 in tmp:
            rec_proc.append(link3.find(class_="recipe-directions__list--item").text)

        rec_proc = ''.join(rec_proc)

        # print("\nrec_proc: '" + rec_proc + "'")

        img = soup.find(class_="rec-photo").get('src')


        urllib.urlretrieve(img, str(counter2 + (last_density * iteration)) + ".jpg")

        data = {}
        data['rec_title'] = rec_title
        data['rec_ing'] = rec_ing
        data['rec_proc'] = rec_proc


        final.append(data)
        print("Finished (" + url + ")\n")
        counter2+=1
    last_density = counter
    page_start-=1
    href_arr = []
    iteration += 1
#resp = urllib.urlopen('http://allrecipes.com/') # open url
#html_doc = resp.read()
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(html_doc, 'html.parser')
#sr0 = soup.find_all("a", href=re.compile("recipe/"))
    
#for sr1 in sr0:
 #   print(sr1.get("href"))




# no_of_pagedowns = 5000

# while no_of_pagedowns:
#     elem.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)
#     no_of_pagedowns-=1

with open('recipes.json', 'w') as outfile:
    json_data = json.dump(final, outfile)
print("Scrape finished!")
