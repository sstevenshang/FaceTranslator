from lxml import html
from lxml.html import tostring
import sqlite3
from bs4 import BeautifulSoup
import requests
import sys



page_url = ("https://www.facebook.com/CatTurtle")

def scrape():
    root = html.parse(page_url)
    soup = BeautifulSoup(tostring(root), 'lxml')
    search_links = root.xpath(".//a[contains(text(), 'Search')]")  # Example use of xpath


    for blah in soup.html.head.find_all("entity_id"):
    	print(blah)




if __name__=="__main__":
	scrape()