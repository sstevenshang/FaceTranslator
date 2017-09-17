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

    

#    print(soup.html.prettify())

#    for blah in soup.html.body.meta.find_all("content"):
#    	print(blah)


#div class="_5h60"
    for hi in soup.find_all(id="pagelet_timeline_main_column"):
       myString = hi['data-gt']
       print(myString[18:myString.find("\"", 18)])

    #print(soup.find_all(id="pagelet_timeline_main_column")[0].contents[0])


if __name__=="__main__":
	scrape()
