from lxml import html
from lxml.html import tostring
from bs4 import BeautifulSoup
import requests
import sys
import urllib2
from urllib2 import HTTPError, URLError
import json



url = 'https://www.facebook.com/keshav.gupta.28/about?lst=100003279925222%3A100018139210752%3A1505647969'

urls = [
	'https://www.facebook.com/keshav.gupta.28/about?lst=100003279925222%3A100018139210752%3A1505647969',
	'https://www.facebook.com/alyssia.jovellanos/about?lst=100003279925222%3A503591958%3A1505649241',
	'https://www.facebook.com/cpellaton/about?lst=100003279925222%3A542778746%3A1505649264',
	'https://www.facebook.com/cyrayden/about?lst=100003279925222%3A554878779%3A1505649369',
	'https://www.facebook.com/gregboerman/about?lst=100003279925222%3A571025972%3A1505649380',
	'https://www.facebook.com/harshita.yerramreddy/about?lst=100003279925222%3A586523567%3A1505649381',
	'https://www.facebook.com/charles.a.malenfant/about?lst=100003279925222%3A596419033%3A1505649402',
	'https://www.facebook.com/benji.pelletier/about?lst=100003279925222%3A618290888%3A1505649403',
	'https://www.facebook.com/vicky.shao.54/about?lst=100003279925222%3A651123274%3A1505649404',
	'https://www.facebook.com/stasrutkowski/about?lst=100003279925222%3A665599561%3A1505649434',
	'https://www.facebook.com/ArtePermacultura/about?lst=100003279925222%3A669255542%3A1505649436',
	'https://www.facebook.com/hamzah.khan.397/about?lst=100003279925222%3A670318163%3A1505649437',
	'https://www.facebook.com/antomasini98/about?lst=100003279925222%3A711777640%3A1505649440'

]

# print(url.find('%3A'))
# print(url.find('%3A', 67))
def getInfo():
	for url in urls:
		theId = url[url.find('%3A')+3:url.find('%3A', url.find('%3A') + 1)]
		name = scrape(theId)

		strBuild = '{\'name\': \'' + name + '\', \'url\': baseUrl + \'' + theId + '\' + endUrl},'


		#print(url[url.find('%3A')+3:url.find('%3A', url.find('%3A') + 1)])
		print(strBuild)


def scrape(uid):
	base_url = "https://graph.facebook.com/"
	token = 'EAACEdEose0cBACbeJ9sCDZBA79ABQM3qHHSEESTYFAA3jVgNj4gNMNyO6dwOOzLGU4u2qc49dUTe7asvZCVgsFUWeY2IbHrZC3gXGgrrpwtTKrPr4HWnvviEvB7uoofd0mvniScGkcvPRvqY6XgHEtpKkZANVfMMbiDkgIC5wWTjnkPIwOaF5WgRZCAuTZAW7t6chHZA0CuIQZDZD'
	url = base_url + uid + "?fields=name&access_token=" + token
	try:
		friendsObj = urllib2.urlopen(url)
		friendsJson = json.loads(friendsObj.read().decode())
		#print(friendsJson.get('name'))
		name = friendsJson.get('name')
	

	except HTTPError as e:
		print("HTTP Error:", e.code, url)
	except URLError as e:
		print("URL Error:", e.reason, url)

	return name
    #print("'name': '" + name + "', 'url': baseUrl + '" + id + "' + endUrl")




if __name__=="__main__":
	getInfo()    