from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import string
from collections import Counter

url = 'https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1'

response = requests.get(url)

sopa = BeautifulSoup(response.text, 'html.parser')

rate_box1 = sopa.find('span', {'class':'ccOutputRslt'}).get_text().replace('EUR',"")
rate1 = float(rate_box1)

rate_box2 = sopa.find('span', {'class':'ccOutputTxt'}).get_text().replace('USD',"")
rate2 = float(rate_box1)

moedas = ['US','EUR','GBP','JPY','AUD']
valores = [rate2,rate1,0.75,11.0,1.25]

plt.bar(moedas, valores)
plt.show()