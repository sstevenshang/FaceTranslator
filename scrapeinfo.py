from lxml import html
from lxml.html import tostring
from bs4 import BeautifulSoup
import requests
import sys
import urllib2
from urllib2 import HTTPError, URLError
import json



# url = 'https://www.facebook.com/keshav.gupta.28/about?lst=100003279925222%3A100018139210752%3A1505647969'

# urls = [
# 	'https://www.facebook.com/keshav.gupta.28/about?lst=100003279925222%3A100018139210752%3A1505647969',
# 	'https://www.facebook.com/alyssia.jovellanos/about?lst=100003279925222%3A503591958%3A1505649241',
# 	'https://www.facebook.com/cpellaton/about?lst=100003279925222%3A542778746%3A1505649264',
# 	'https://www.facebook.com/cyrayden/about?lst=100003279925222%3A554878779%3A1505649369',
# 	'https://www.facebook.com/gregboerman/about?lst=100003279925222%3A571025972%3A1505649380',
# 	'https://www.facebook.com/harshita.yerramreddy/about?lst=100003279925222%3A586523567%3A1505649381',
# 	'https://www.facebook.com/charles.a.malenfant/about?lst=100003279925222%3A596419033%3A1505649402',
# 	'https://www.facebook.com/benji.pelletier/about?lst=100003279925222%3A618290888%3A1505649403',
# 	'https://www.facebook.com/vicky.shao.54/about?lst=100003279925222%3A651123274%3A1505649404',
# 	'https://www.facebook.com/stasrutkowski/about?lst=100003279925222%3A665599561%3A1505649434',
# 	'https://www.facebook.com/ArtePermacultura/about?lst=100003279925222%3A669255542%3A1505649436',
# 	'https://www.facebook.com/hamzah.khan.397/about?lst=100003279925222%3A670318163%3A1505649437',
# 	'https://www.facebook.com/antomasini98/about?lst=100003279925222%3A711777640%3A1505649440'
# 'https://www.facebook.com/kothariaditya7/about?lst=100003279925222%3A770860233%3A1505650597',
# 'https://www.facebook.com/vaibzishere/about?lst=100003279925222%3A850725005%3A1505650601',
# 'https://www.facebook.com/notmahi/about?lst=100003279925222%3A1011395336%3A1505650602',
# 'https://www.facebook.com/Catheryn.Li/about?lst=100003279925222%3A1016013452%3A1505650604',
# 'https://www.facebook.com/chen.x.dawn/about?lst=100003279925222%3A1027604391%3A1505650676',
# 'https://www.facebook.com/rebca.vandeven/about?lst=100003279925222%3A1030208314%3A1505650679',
# 'https://www.facebook.com/daniyal.waitforit.ahmed/about?lst=100003279925222%3A1065739636%3A1505650688',
# 'https://www.facebook.com/edward.she/about?lst=100003279925222%3A1114555158%3A1505650816',
# 'https://www.facebook.com/RoiSinoff/about?lst=100003279925222%3A1167596300%3A1505650821',
# 'https://www.facebook.com/evonnengineer/about?lst=100003279925222%3A1210777741%3A1505650827',
# 'https://www.facebook.com/ligier.michael/about?lst=100003279925222%3A1229049259%3A1505650854',
# 'https://www.facebook.com/jonxmak/about?lst=100003279925222%3A1238531143%3A1505650855',
# 'https://www.facebook.com/kastan.day/about?lst=100003279925222%3A1247533932%3A1505650859',
# 'https://www.facebook.com/mrkevinshum/about?lst=100003279925222%3A1252966223%3A1505650860'
	# 'https://www.facebook.com/faridasabry/about?lst=100003279925222%3A1342823696%3A1505651384',
	# 'https://www.facebook.com/mwang97/about?lst=100003279925222%3A1325535406%3A1505651386',
	# 'https://www.facebook.com/alyssa.chen.39/about?lst=100003279925222%3A1320032131%3A1505651387',
	# 'https://www.facebook.com/zhao.li.XD/about?lst=100003279925222%3A1310735205%3A1505651388',
	# 'https://www.facebook.com/apasp/about?lst=100003279925222%3A1422675265%3A1505651442',
	# 'https://www.facebook.com/leononme/about?lst=100003279925222%3A1455503088%3A1505651446',
	# 'https://www.facebook.com/kartikye.mittal/about?lst=100003279925222%3A1457300650%3A1505651447',
	# 'https://www.facebook.com/wangtiffanysj/about?lst=100003279925222%3A1463569628%3A1505651450',
	# 'https://www.facebook.com/kavitha.dee.9/about?lst=100003279925222%3A1478034418%3A1505651451'

# ]

urls = [
	'https://www.facebook.com/kimmyheartsyou/about?lst=100003279925222%3A1481127456%3A1505651822',
	'https://www.facebook.com/lance.mccarthy/about?lst=100003279925222%3A1484328157%3A1505651823',
	'https://www.facebook.com/sean.km.bae/about?lst=100003279925222%3A1492027223%3A1505651824',
	'https://www.facebook.com/jason.jin.98/about?lst=100003279925222%3A1505772254%3A1505651824',
	'https://www.facebook.com/kxin.zhang/about?lst=100003279925222%3A1507772617%3A1505651825',
	'https://www.facebook.com/ksf.kennethfriedman/about?lst=100003279925222%3A1515890562%3A1505651871',
	'https://www.facebook.com/karumanchi.pradeep/about?lst=100003279925222%3A1518466071%3A1505651872',
	'https://www.facebook.com/adityavkhanna/about?lst=100003279925222%3A1529203443%3A1505651875',
	'https://www.facebook.com/charleslu1/about?lst=100003279925222%3A1532187221%3A1505651876',
	'https://www.facebook.com/meepitschree/about?lst=100003279925222%3A1543441270%3A1505651880',
	'https://www.facebook.com/lisamonique.edward/about?lst=100003279925222%3A1544137080%3A1505651882',
	'https://www.facebook.com/rebecca.ansems/about?lst=100003279925222%3A1586653091%3A1505651925',
	'https://www.facebook.com/kittylilycat/about?lst=100003279925222%3A1598960421%3A1505651928',
	'https://www.facebook.com/nwchen.me/about?lst=100003279925222%3A1626843875%3A1505651931',
	'https://www.facebook.com/michelle.yuen.585/about?lst=100003279925222%3A1629441632%3A1505651933',
	'https://www.facebook.com/akshit.singla/about?lst=100003279925222%3A1684253978%3A1505651937'

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