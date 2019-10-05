from bs4 import BeautifulSoup
import urllib.request 
import re
from inscriptis import get_text
import os
import simplejson

url = "https://career.guru99.com/top-50-html-interview-questions/ "

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")

soup = BeautifulSoup(page,'lxml')

for data in soup.find_all("p"):
    results = []
    results.append( data.text.strip())
    print(results)

    with open('data.txt', 'w') as file:
         for item in results:
             file.write("{}\n".format(item))
           # file.write(str(soup))