import requests
from bs4 import BeautifulSoup as bs
import mysql.connector
import getpass

a = input("please enter car name in following format: 'brand model' or 'brand' ")
a = a.split()
a = "/".join(a)
url = 'https://www.truecar.com/used-cars-for-sale/listings/%s/' % (a)

def get_price_and_milage(url):
    response = requests.get(url)
    restext = response.text
    soup = bs(restext, 'html.parser')
    posts = soup.find_all('a', class_ = 'linkable vehicle-card-overlay order-2')
    postsurl = []
    for post in posts[:20]:
        #print(post.attrs['href'])
        postsurl.append('https://www.truecar.com' + post.attrs['href'])
    
    global priceandmilage
    priceandmilage = []

    for url in postsurl:
        response = requests.get(url)
        restext = response.text
        soup = bs(restext, 'html.parser')
        title = soup.find('div', class_="heading-3_5 normal-case heading-md-2 md:normal-case grow leading-[1.2] mb-1")
        title = title.text
        title = title.strip()
        #r(\d{4})\s(\w.*?\s\w.*?)\s(\w.*)
        milage = soup.find_all('div', class_ = 'mb-3 lg:mb-4 col-12 col-lg-6', limit=2)
        milage = milage[1]
        milage = milage.text
        milage = milage.strip()
        price = soup.find_all('div', {'data-test':"vdpPricingInfoPrice"}, limit=2)
        price = price[1]
        price = price.text
        price = price.strip()
        print('{} - {} - {}'.format(title, milage, price))
        priceandmilage.append([title, milage, price])

def connectandwrite(lst):
    while True:
        dbname = input("Please Enter Your Database Name: ")
        passw = getpass.getpass('Please Enter Your root Password: ')
        #print('Connecting ')
        try:
            cnx = mysql.connector.connect(user='root',
                                        password=passw,
                                        host='127.0.0.1',
                                        database=dbname)
            curser = cnx.cursor()
            print("Connected")
            break
        except:
            print('Wrong password or database name')
            continue

    table = input("Please Entre Your Table Name: ")        
    for i,j,k in lst:
        try:   
            curser.execute("INSERT INTO %s VALUES ('%s', '%s', '%s')" % (table, i, j, k))
            cnx.commit()
        except:
            print("Table '%s' doesn't exist" % (table))
            cnx.close()
            exit()
    print("values inserted into %s table of %s database successfully" % (table, dbname))
    cnx.close()


get_price_and_milage(url)
connectandwrite(priceandmilage)