import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import requests
import mysql.connector
import re
import random

def connect():
    while True:
        dbname = 'cars'
        username = 'root'
        passw = '1230'

        try:
            global cnx
            global curser
            cnx = mysql.connector.connect(user=username,
                                        password=passw,
                                        host='127.0.0.1',
                                        database=dbname)
            curser = cnx.cursor()
            print('Connected')
            break

        except:
            print('Wrong password, username or database name')
            exit()

def write(i):
    table = 'cars' 
    try:
        curser.execute('''INSERT IGNORE INTO %s VALUES ("%s", "%s", "%s", "%s", "%s", %i, %i)''' % (table, i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        cnx.commit()
    except:
        pass
def request(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.page_load_strategy = 'none'
    driver = Chrome(options=options)
    driver.implicitly_wait(5)
    try:
        driver.get(url)
        time.sleep(round(random.uniform(12, 1), 2))
    finally:
        return driver
    

connect()
urls = []
posturls = []

for i in range(1, 30):
    url = 'https://www.truecar.com/used-cars-for-sale/listings/?page=%i' %(i)
    urls.append(url)

for url in urls:
    print(url, "##################################################")
    response = requests.get(url)
    restext = response.text
    soup = bs(restext, 'html.parser')
    posts = soup.find_all('a', class_ = 'linkable vehicle-card-overlay order-2')
    postsurl = []
    for post in posts:
        print(post.attrs['href'])
        url = 'https://www.truecar.com' + post.attrs['href']
        driver = request(url)
        title = driver.find_element(By.CSS_SELECTOR, "div[class*='heading-3_5 normal-case heading-md-2 md:normal-case grow leading-[1.2] mb-1'")
        title = title.text
        print(title)
        title = title.replace("\'", "")
        title = title.replace("\"", "")
        title = title.strip()
        title = re.match(r'(\d{4})\s(\w.*?)\s(\w.*?)\s(\w.*)', title)
        year = title[1]
        brand = title[2]
        model = title[3]
        detail = title[4]
        #---------------------------------
        locmilecolor = driver.find_elements(By.CSS_SELECTOR, "div[class='mb-2 lg:mb-3 col-12 col-lg-6'")
        color = locmilecolor[0].text
        color = color.replace('Exterior: ', '')
        color = color.strip()
        milage = locmilecolor[2].text
        milage = milage.strip()
        milage = milage.replace(",", "")
        milage = milage.replace(" miles", "")
        milage = int(milage)
        print(milage)
        price = driver.find_elements(By.CSS_SELECTOR, "div[data-test='vdpPricingInfoPrice'")
        price = price[1].text
        price = price.replace("$", "")
        price = price.replace(",", "")
        price = int(price)
        print(price)
        lst = [brand, model, detail, year, color, milage, price]
        write(lst)
        driver.close()