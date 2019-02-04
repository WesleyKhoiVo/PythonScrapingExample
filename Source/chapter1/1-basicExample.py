# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:34:56 2019

@author: khoim
"""

from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.read())