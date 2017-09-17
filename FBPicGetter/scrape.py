from lxml import html
from lxml.html import tostring
import sqlite3
from bs4 import BeautifulSoup
import requests
import sys
import urllib.request



page_url = ("https://www.facebook.com/CatTurtle")

def scrape():
    root = urllib.request.urlopen(page_url)

    request = requests.get(page_url)
    soup = BeautifulSoup(root, 'lxml')

    

    print(soup.html.body.div)

    for blah in soup.html.body.div.find_all("entity_id"):
    	print(blah)




if __name__=="__main__":
	scrape()
