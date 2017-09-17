import httplib, urllib, base64, json, sys

nameKeySet = []
justNames = []

baseUrl = 'https://graph.facebook.com/'
endUrl = '/picture?type=large'

#{'name': '', 'url': ''},

peopleIds = {'Tristan Wiley': '100000250991175',
'Abigail Gomez': '100021687960888',
'Timothy Glinski': '100011600352566',
'Darius Bopp': '100015093614245',
'Kendyll Hicks ': '100011269059197',
'Tejasvi Nareddy ': '100009254604287',
'Kyle Swanson': '100000603823463',
'Laura Eckman': '100000401767973',
'Aaron Vontell': '100000350713059',
'Yasmeen Roumie': '100009219651315',
'Rohan Shah': '1475570764',
'Nadia Asif': '100007984215053',
'Alvin Zhang': '100009871129330',
'Meghan Davis': '100009851710081',
'Ajay Ramesh': '100009428228709',
'Charles Vorbach': '100008404685491',
'Justin Wei': '100008315821612',
'Alyssia Jovellanos': '503591958',
'Cooper Pellaton': '542778746',
'Charles Antoine Malenfant': '596419033',
'Benji Pelletier': '618290888',
'Vicky Shao': '651123274',
'Stas Rutkowski': '665599561',
'Antonella Masini': '711777640',
'Vaibhav Gupta': '850725005',
'Mahi Nur Muhammad': '1011395336',
'Dawn Chen Xi': '1027604391',
'Rebca van de Ven': '1030208314',
'Daniyal Ahmed': '1065739636',
'Farida Sabry': '1342823696',
'Michael Wang': '1325535406',
'Kartikye Mittal': '1457300650',
'Kavitha Dhanukodi': '1478034418',
'Kimberli Zhong': '1481127456',
'Lance McCarthy': '1484328157',
'Sean Bae': '1492027223',
'Kexin Zhang': '1507772617',
'Kenny Friedman': '1515890562',
'Karumanchi Pradeep': '1518466071',
'Aditya Khanna': '1529203443',
'Christie Xu': '1543441270',
'Lily Chen': '1598960421',
'Akshit Singla': '1684253978',
'Justin Wei': '100008315821612',
'Vinay Kasat': '100003006012440',
'Bill Chen': '100003049323816',
'Claire Nord': '100001735263697',
'Neena Dugar': '100001360088260',
'Edwin Zhang': '520511148',
'Noah Moroze': '100003046714844',
'Campion Fellin': '100003279925222',
'John Tran': '100002630705962',
'Steven Shang': '100004054732119'}

peopleInfo = [
{'name': 'Tristan Wiley', 'url': baseUrl + '100000250991175' + endUrl},
{'name': 'Abigail Gomez', 'url': baseUrl + '100021687960888' + endUrl},
{'name': 'Timothy Glinski ', 'url': baseUrl + '100011600352566' + endUrl},
{'name': 'Darius Bopp', 'url': baseUrl + '100015093614245' + endUrl},
{'name': 'Kendyll Hicks ', 'url': baseUrl + '100011269059197' + endUrl},
{'name': 'Tejasvi Nareddy ', 'url': baseUrl + '100009254604287' + endUrl},
{'name': 'Kyle Swanson', 'url': baseUrl + '100000603823463' + endUrl},
{'name': 'Laura Eckman', 'url': baseUrl + '100000401767973' + endUrl},
{'name': 'Aaron Vontell', 'url': baseUrl + '100000350713059' + endUrl},
{'name': 'Yasmeen Roumie', 'url': baseUrl + '100009219651315' + endUrl},
{'name': 'Rohan Shah', 'url': baseUrl + '1475570764' + endUrl},
{'name': 'Nadia Asif', 'url': baseUrl + '100007984215053' + endUrl},
{'name': 'Alvin Zhang', 'url': baseUrl + '100009871129330' + endUrl},
{'name': 'Meghan Davis', 'url': baseUrl + '100009851710081' + endUrl},
{'name': 'Ajay Ramesh', 'url': baseUrl + '100009428228709' + endUrl},
{'name': 'Charles Vorbach', 'url': baseUrl + '100008404685491' + endUrl},
{'name': 'Justin Wei', 'url': baseUrl + '100008315821612' + endUrl},
{'name': 'Claire Nord', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/18519733_1335827749818388_3894574777309830985_n.jpg?oh=1e86a33d0a011489badf09df9bced386&oe=5A479644'},
{'name': 'Neena Dugar', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/18034259_1270208539701137_7174658807392622290_n.jpg?oh=bd2beb442769bf932fbc868b531adb19&oe=5A505F72'},
{'name': 'Claire Nord', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/11753696_852597408141427_5759840540926367897_n.jpg?oh=1273cfc201f4d6072d6ef9343d0a32a3&oe=5A5E2607'},
{'name': 'Claire Nord', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/18121068_211028609392990_7566083850424525968_o.jpg?oh=cf985164021dc12c0d9bc553687c5b6a&oe=5A43BC5E'},
{'name': 'Claire Nord', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/15844329_10211576253626060_42006846960767823_o.jpg?oh=0696bc0e57b4036baf709c5e2aba0c65&oe=5A583A4D'},
{'name': 'Neena Dugar', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/1609985_951325954922732_1558298101812096661_n.jpg?oh=f69b5cdb977768290b0bd9a938bba8e5&oe=5A520974'},
{'name': 'Edwin Zhang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/72387_10153513202191149_7418486409646845092_n.jpg?oh=d8200941e68c33bbbc06475a4c959d2f&oe=5A59270F'},
{'name': 'Edwin Zhang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/12524350_552771424883588_162302374307473142_n.jpg?oh=fabed4e05b5b009457262dcb1d8b93fa&oe=5A4EECBB'},
{'name': 'Edwin Zhang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/12832463_552771428216921_2809021755299480682_n.jpg?oh=992da27175b049490eeca962c0f9e5b7&oe=5A4B884E'},
{'name': 'Edwin Zhang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/1910109_1090402091000319_6253408302782601196_n.jpg?oh=92f479996a6c1473bd80cc5cfd2aa292&oe=5A57521F'},
{'name': 'Edwin Zhang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/1910109_1090402091000319_6253408302782601196_n.jpg?oh=92f479996a6c1473bd80cc5cfd2aa292&oe=5A57521F'},

{'name': 'Alyssia Jovellanos', 'url': baseUrl + '503591958' + endUrl},
{'name': 'Cooper Pellaton', 'url': baseUrl + '542778746' + endUrl},
{'name': 'Charles Antoine Malenfant', 'url': baseUrl + '596419033' + endUrl},
{'name': 'Benji Pelletier', 'url': baseUrl + '618290888' + endUrl},
{'name': 'Vicky Shao', 'url': baseUrl + '651123274' + endUrl},
{'name': 'Stas Rutkowski', 'url': baseUrl + '665599561' + endUrl},
{'name': 'Antonella Masini', 'url': baseUrl + '711777640' + endUrl},
{'name': 'Vaibhav Gupta', 'url': baseUrl + '850725005' + endUrl},
{'name': 'Mahi Nur Muhammad', 'url': baseUrl + '1011395336' + endUrl},
{'name': 'Dawn Chen Xi', 'url': baseUrl + '1027604391' + endUrl},
{'name': 'Rebca van de Ven', 'url': baseUrl + '1030208314' + endUrl},
{'name': 'Daniyal Ahmed', 'url': baseUrl + '1065739636' + endUrl},
{'name': 'Farida Sabry', 'url': baseUrl + '1342823696' + endUrl},
{'name': 'Michael Wang', 'url': baseUrl + '1325535406' + endUrl},
{'name': 'Kartikye Mittal', 'url': baseUrl + '1457300650' + endUrl},
{'name': 'Kavitha Dhanukodi', 'url': baseUrl + '1478034418' + endUrl},
{'name': 'Kimberli Zhong', 'url': baseUrl + '1481127456' + endUrl},
{'name': 'Lance McCarthy', 'url': baseUrl + '1484328157' + endUrl},
{'name': 'Sean Bae', 'url': baseUrl + '1492027223' + endUrl},
{'name': 'Kexin Zhang', 'url': baseUrl + '1507772617' + endUrl},
{'name': 'Kenny Friedman', 'url': baseUrl + '1515890562' + endUrl},
{'name': 'Karumanchi Pradeep', 'url': baseUrl + '1518466071' + endUrl},
{'name': 'Aditya Khanna', 'url': baseUrl + '1529203443' + endUrl},
{'name': 'Christie Xu', 'url': baseUrl + '1543441270' + endUrl},
{'name': 'Lily Chen', 'url': baseUrl + '1598960421' + endUrl},
{'name': 'Akshit Singla', 'url': baseUrl + '1684253978' + endUrl},
{'name': 'Justin Wei', 'url': baseUrl + '100008315821612' + endUrl},
{'name': 'Noah Moroze', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/14316909_921695414608674_7882783706517828815_n.jpg?oh=5743b1ef371ac18a0673ade5d32dd195&oe=5A5C45A7'},
{'name': 'Vinay Kasat', 'url': baseUrl + '100003006012440' + endUrl},
{'name': 'Bill Chen', 'url': baseUrl + '100003049323816' + endUrl},


{'name': 'Campion Fellin', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/17390379_1260031627449489_8802200252481370085_o.jpg?oh=c4275f373e6c4d52bf4e1b8eed745e59&oe=5A4E0338'},
{'name': 'Campion Fellin', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/14066351_1050128121773175_9182664610036581040_o.jpg?oh=593b99c31ad8de65600ae950d13a2068&oe=5A4A7D8D'},
{'name': 'Campion Fellin', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/12238164_880875425365113_1210886991989294426_o.jpg?oh=1060949473847177dc0f3c5fb74f8e0e&oe=5A4D5609'},
{'name': 'Campion Fellin', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/11024678_763791060406884_5211712562033115495_o.jpg?oh=6bce7862e00379a766b697006f86f879&oe=5A44BE3B'},

{'name': 'John Tran', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/16804237_1170004756430537_6581281884737186499_o.jpg?oh=e07bce552888d3b339664e15a8bf1209&oe=5A40BB43'},
{'name': 'John Tran', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/13244261_939245159506499_4022522226824089791_o.jpg?oh=5aa0f305d66e10116de106e1d2bf447c&oe=5A483B2C'},
{'name': 'John Tran', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/12469635_871775769586772_1684702532372109528_o.jpg?oh=4a8dc9a6ecf5760eefccf1a6c182cce8&oe=5A1481CF'},
{'name': 'John Tran', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/10518589_607921892638829_5647906411012524774_o.jpg?oh=1c6a69dcdbb6d5115390451a33ffd71b&oe=5A54A65B'},
{'name': 'John Tran', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/18671532_1568200906526462_2606737617372728044_o.jpg?oh=014a265de67470be0ca74c2f2026087c&oe=5A4F3957'},


{'name': 'Steven Shang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/13428012_937148863096929_2055810890344721622_n.jpg?oh=e431430c19b0267060623e5dea4754ed&oe=5A4C0369'},
{'name': 'Steven Shang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/10476337_599512846860534_5936298291930122475_o.jpg?oh=ae897bcf39b57007b2db3646615c96be&oe=5A141532'},
{'name': 'Steven Shang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/221553_114193865392437_286718916_o.jpg?oh=2699ec26bd017501b51ef7d7601749fd&oe=5A500364'},
{'name': 'Steven Shang', 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t1.0-9/10613126_538016859676800_2524068398576153713_n.jpg?oh=33cfb77fff3591a75a1df20f0889ca52&oe=5A3F2073'},

{'name': 'Marty McFly', 'url': 'https://upload.wikimedia.org/wikipedia/en/d/d8/Michael_J._Fox_as_Marty_McFly_in_Back_to_the_Future%2C_1985.jpg'},
{'name': 'Marty McFly', 'url': 'https://www.sideshowtoy.com/assets/products/902499-marty-mcfly/lg/back-to-the-future-2-marty-mcfly-sixth-scale-hot-toys-902499-08.jpg'},
{'name': 'Marty McFly', 'url': 'https://www.sideshowtoy.com/photo_902234_thumb.jpg'},
{'name': 'Marty McFly', 'url': 'http://majorspoilers.com/wp-content/uploads/2015/10/Back-To-The-Future-1.png'},
{'name': 'Marty McFly', 'url': 'https://pbs.twimg.com/profile_images/661421083501961216/ymbKz_05.jpg'},
{'name': 'Doc Brown', 'url': 'https://i.pinimg.com/736x/a6/08/c9/a608c945bb79dbdc2153cd77ec652b11--doc-brown-costume-emmett-brown.jpg'},
{'name': 'Doc Brown', 'url': 'https://upload.wikimedia.org/wikipedia/en/9/97/Doc_Brown.JPG'},
{'name': 'Doc Brown', 'url': 'https://moviewriternyu.files.wordpress.com/2015/10/doc-3.jpg'},
{'name': 'Doc Brown', 'url': 'http://www.cinema52.com/2013/wp-content/uploads/2013/07/20130731-165540.jpg'},

{'name': 'Steve Huffman', 'url': 'http://a.abcnews.com/images/Technology/ht_steve_huffman_reddit_jc_150715_4x3_992.jpg'},
{'name': 'Steve Huffman', 'url': 'http://assets.uvamagazine.org/images/uploads/2014/03-Fall/Features/Reddit/SteveHuffman.png'},
{'name': 'Steve Huffman', 'url': 'http://press.hipmunk.com/headshots/steve_huffman.jpg'},
{'name': 'Steve Huffman', 'url': 'http://speakerdata.s3.amazonaws.com/photo/image/840148/.i.0.steve-huffman-hipmunk-my-phone.jpg'},
{'name': 'Steve Huffman', 'url': 'https://heavyeditorial.files.wordpress.com/2016/11/huffman-e1480090604940.jpg?quality=65&strip=all'},
{'name': 'Steve Huffman', 'url': 'https://cdn.vox-cdn.com/thumbor/CwRpfyhz6m94n9seLP-B4QpN4MI=/0x0:7015x4682/1200x800/filters:focal(2163x1193:3285x2315)/cdn.vox-cdn.com/uploads/chorus_image/image/52242883/reddit_steve_huffman_close.0.jpeg'},

{'name': 'Kyle Vogt', 'url': 'https://media.licdn.com/mpr/mpr/shrinknp_200_200/p/6/005/069/0cf/3b56c47.jpg'},
{'name': 'Kyle Vogt', 'url': 'https://i.ytimg.com/vi/YZ2UMgyABt0/maxresdefault.jpg'},
{'name': 'Kyle Vogt', 'url': 'https://media.bizj.us/view/img/2717071/b7j7qfkzsoaa2foacfajxp30kihx3uw8tdsxr6agkhe*750xx574-324-0-77.png'},
{'name': 'Kyle Vogt', 'url': 'https://www.incimages.com/30under30/2009/photos/9_Kyle-Justin-TV-BKT.jpg'},
{'name': 'Kyle Vogt', 'url': 'http://www.autonews.com/apps/pbcsi.dll/storyimage/CA/20170402/UNDER4001/304039974/AR/0/AR-304039974.jpg'},

{'name': 'Steve Jobs', 'url': 'https://www.biography.com/.image/c_fill%2Ccs_srgb%2Cg_face%2Ch_300%2Cq_80%2Cw_300/MTE5NDg0MDU0NTIzODQwMDE1/steven-jobs-9354805-2-402.jpg'},
{'name': 'Steve Jobs', 'url': 'https://images-na.ssl-images-amazon.com/images/I/81VStYnDGrL.jpg'},
{'name': 'Steve Jobs', 'url': 'https://www.technobezz.com/files/uploads/2015/10/stevejobs1.jpg'},
{'name': 'Steve Jobs', 'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuDxwmahKY0XbJno9uiibbsvyFboIvcX4Jwz5v_PQGzbZQ3cZ9vw'},
{'name': 'Steve Jobs', 'url': 'http://static5.businessinsider.com/image/54e75c79eab8ea2e0cd8ea8d/in-1982-steve-jobs-presented-an-amazingly-accurate-theory-about-where-creativity-comes-from.jpg'}


]


headers = {
    # Request headers.
    'Content-Type': 'application/json',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '37e02440a4dd4ef2b738acf9e5dd46ac',
}

def main():

    everyone = getEveryone()
    #print(everyone)

    for identity in everyone:
        justNames.append(identity['name'])
        nameKeySet.append([identity['name'], identity['personId']])

    for person in peopleInfo:
        #print(person['name'])
        print("adding this person: " + person['name'])
        if (person['name'] in justNames):
            #print("User already exists, adding photo")
            for identity in nameKeySet:
                if (identity[0] == person['name']):
                    #print("******")
                    #print(person['name'])
                    addFace(identity[1], person['url'])
        else:
            #print("New User")
            #print("**********")
            #print(person['name'])
            justNames.append(person['name'])
            addPerson(person['name'], True, person['url'], peopleIds.get(person['name']))



def getEveryone():
    body = "{}"
    try:
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/firstgroupid/persons", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())

	    #print(response.reason)
        #print(data)
        #sys.exit(0)
        return data
	    #print(response)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))




def addPerson(name, isNew, imageURL, uid):
    if uid == None:
        print("shit")
        uid = "1234"

    body = "{ 'name': '" + name + "', 'userData':" + uid + "}"
    try:

        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/firstgroupid/persons", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())

        #print(response.reason)
        #print(data['personId'])
        #print(response)
        if (isNew):
            nameKeySet.append([name, data['personId']])
            addFace(data['personId'],imageURL)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def findPersonFromId(uid):
    everyone = getEveryone()
    for person in everyone:
        if (person['personId'] == uid):
            print(person['name'])

def addFace(who, imageURL):
    personId = who
    #body = "{ 'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/14066351_1050128121773175_9182664610036581040_o.jpg?oh=593b99c31ad8de65600ae950d13a2068&oe=5A4A7D8D'}"
    body = "{'url':'" + imageURL + "'}"
    try:

        #personId = "10c69ca3-3c4b-427b-b777-a4c8582df20c"
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/firstgroupid/persons/%s/persistedFaces" % personId, body, headers)
        response = conn.getresponse()
        data = response.read()

    
        #print(response.reason)
        if ("Bad" in response.reason):
            print('bad person: ')
            findPersonFromId(who)
        #print(data)
        #print(response)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def deleteAll():
    everyone = getEveryone()
    for person in everyone:
        print("deleting: " + person['name'])
        deletePerson(person['personId'])


def deletePerson(person):
    body = ""
    try:

        personId = person
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("DELETE", "/face/v1.0/persongroups/firstgroupid/persons/%s" % personId, body, headers)
        response = conn.getresponse()
        data = response.read()

        print(response.reason)
        print(data)
        #print(response)

        conn.close()
    except Exception as e:
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))



def train():
    body = ""
    try:

        #personId = "10c69ca3-3c4b-427b-b777-a4c8582df20c"
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/firstgroupid/train", body, headers)
        response = conn.getresponse()
        data = response.read()

        print(response.reason)
        print(data)
        #print(response)

        conn.close()
    except Exception as e:
        print("in here")
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getStatus():
    body = ""
    try:

        #personId = "10c69ca3-3c4b-427b-b777-a4c8582df20c"
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/firstgroupid/training", body, headers)
        response = conn.getresponse()
        data = response.read()

        # print(response.reason)
        print(data)
        #print(response)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def makePersonGroup():
    try:

        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("PUT", "/face/v1.0/persongroups/firstgroupid/", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())

        #print(response.reason)
        #print(data)


        #print(response)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))







if __name__=="__main__":
	main()
    #deleteAll()

    # train()
    # getStatus()