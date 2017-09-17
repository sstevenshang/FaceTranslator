from lxml import html
from lxml.html import tostring
import sqlite3
from bs4 import BeautifulSoup
import requests
import sys
import urllib.request

page_url = ("https://www.facebook.com/sstevenshang")

def scrape():
    root = urllib.request.urlopen(page_url)

    request = requests.get(page_url)
    soup = BeautifulSoup(root, 'lxml')

    for hi in soup.find_all(id="pagelet_timeline_main_column"):
       id = hi['data-gt']
       print(id[18:id.find("\"", 18)])

    name = str(soup.find_all(id="pageTitle"))
    print(name[23:name.find("|", 23)])


if __name__=="__main__":
	scrape()
