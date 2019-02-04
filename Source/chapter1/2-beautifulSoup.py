# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:45:32 2019

@author: khoim
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)