from bs4 import BeautifulSoup
import requests
import function
import time
import random


url = "https://www.melon.com/chart/index.htm"

headers = {
   'Host': 'www.melon.com',
   'If-None-Match' : "0:b170",
   'Referer': 'https://www.melon.com/index.htm',
   'Upgrade-Insecure-Requests':'1',
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.get(url, headers = headers).text


Soup = BeautifulSoup(html, 'html.parcer') 
ranks = ("#lp3 div.span.rank")


for i in soup 

