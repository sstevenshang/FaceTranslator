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

def getProfiles():
    return profiles

if __name__=="__main__":
    page_urls = ["https://www.facebook.com/sstevenshang","https://www.facebook.com/jj4192", "https://www.facebook.com/futurebitleadership",
        "https://www.facebook.com/CatTurtle", "https://www.facebook.com/max.kessler.50", "https://www.facebook.com/sirhype?pnref=lhc.unseen",
        "https://www.facebook.com/mewsicat", "https://www.facebook.com/moin1998?pnref=lhc.friends", "https://www.facebook.com/profile.php?id=100021687960888"
        ,"https://www.facebook.com/helentheread"]

    for page_url in page_urls:
        scrape(page_url)

    print(profiles)
    getProfiles()
