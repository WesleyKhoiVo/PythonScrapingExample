# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:23:59 2019

@author: khoim
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
allText = bsObj.findAll(id="text")
print(allText[0].get_text())