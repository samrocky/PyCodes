import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.sheypoor.com/s/iran'
x = requests.get('https://divar.ir/s/tehran')
x = x.text
soup = BeautifulSoup(x, 'html.parser')
#soup = soup.find('div', attrs={'class': 'SMz-b'}) #, string= 'توافقی')
print(soup)

#class="SMz-b"