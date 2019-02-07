# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:40:51 2019

@author: khoim
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)