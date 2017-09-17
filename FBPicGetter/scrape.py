from lxml import html
from lxml.html import tostring
from bs4 import BeautifulSoup
import requests
import sys
import urllib.request

profiles = {}

def scrape(page_url):
    root = urllib.request.urlopen(page_url)

    request = requests.get(page_url)
    soup = BeautifulSoup(root, 'lxml')

    for hi in soup.find_all(id="pagelet_timeline_main_column"):
       id = hi['data-gt']
       id = id[18:id.find("\"", 18)]

    name = str(soup.find_all(id="pageTitle"))
    name = name[23:name.find("|", 23)]

    profiles[id] = name
    print("'name': '" + name + "', 'url': baseUrl + '" + id + "' + endUrl")


def getProfiles():
    return profiles

if __name__=="__main__":
    page_urls = ["https://www.facebook.com/100003006012440", "https://www.facebook.com/billchen99"]


    for page_url in page_urls:
        scrape(page_url)

    getProfiles()
