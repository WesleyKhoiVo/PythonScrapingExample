# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:44:02 2019

@author: khoim
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling) 