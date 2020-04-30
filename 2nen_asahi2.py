# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 06:40:01 2020

@author: USER
"""

import requests
from bs4 import BeautifulSoup

load_url = "https://www.asahi.com/articles/DA3S14459819.html?iref=pc_rensai_long_16_article"
html = requests.get(load_url)

soup = BeautifulSoup(html.content,"html.parser")

topic1 = soup.find(class_ ="Title")
topic2 = soup.find(class_ ="ArticleText")

print(topic1.text)
print(topic2.text)