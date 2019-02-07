# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 11:51:45 2019

@author: khoim
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])