from bs4 import BeautifulSoup
import requests

url = ""https://play.google.com/store/apps/category/...""
res = requests.get(url) # responce
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select ('div.card-list')

print(">>>>>>>", len(card_list), card_list[0].get('class'))
for i in card_list:
    cards = i.select('.card')
    print("LLL>>", LEN(CARDS))
    for c in cards:
        print(">>", c.get('class'), c.selct('a.title')[0].text)