import requests
from bs4 import BeautifulSoup

url = "https://www.sheypoor.com/s/iran/home?c=43608&vl=1/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", class_="SMz-b")
print(posts)

'''for post in posts:
    title = post.find("span", class_="post-card__title")
    description = post.find("span", class_="post-card__description")
    price = post.find("span", class_="post-card__price")
    if price and price.text == "توافقی":
        print(title.text)
        print(description.text)
        print(price.text)
        print("-" * 20)
'''