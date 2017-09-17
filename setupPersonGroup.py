import httplib, urllib, base64, json, sys

nameKeySet = []
justNames = []

baseUrl = 'https://graph.facebook.com/'
endUrl = '/picture?type=large'

peopleInfo = [
{'name': 'Jenny Li', 'url': baseUrl + '1463239405' + endUrl},
{'name': 'Max Kessler', 'url': baseUrl + '100012701701839' + endUrl},
{'name': 'John Tran', 'url': baseUrl + '100002630705962' + endUrl},
{'name': 'Tristan Wiley', 'url': baseUrl + '100000250991175' + endUrl},
{'name': 'Moin Nadeem', 'url': baseUrl + '1378665934' + endUrl},
{'name': 'Abigail Gomez', 'url': baseUrl + '100021687960888' + endUrl},
{'name': 'Lawrence Yan', 'url': baseUrl + '100001148022412' + endUrl},
{'name': 'Helen Read ', 'url': baseUrl + '100010677484404' + endUrl},
{'name': 'Steven  Shang', 'url': baseUrl + '100004054732119' + endUrl},
{'name': 'Silvia Knappe', 'url': baseUrl + '100007016496050' + endUrl}
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
        if (person['name'] in justNames):
            print("yay")
            for identity in nameKeySet:
                if (identity[0] == person['name']):
                    addFace(identity[1], person['url'])
        else:
            print("niiice")
            justNames.append(person['name'])
            addPerson(person['name'], True, person['url'])



def getEveryone():
	body = "{}"
	try:
	    conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
	    conn.request("GET", "/face/v1.0/persongroups/firstgroupid/persons", body, headers)
	    response = conn.getresponse()
	    data = json.loads(response.read())

	    #print(response.reason)
	    #print(data)

	    return data
	    #print(response)

	    conn.close()
	except Exception as e:
	    print("[Errno {0}] {1}".format(e.errno, e.strerror))




def addPerson(name, isNew, imageURL):

    body = "{ 'name': '" + name + "', 'userData':'generic information I guess' }"
    try:

        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/firstgroupid/persons", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())

        #print(response.reason)
        print(data['personId'])
        #print(response)
        if (isNew):
            nameKeySet.append([name, data['personId']])
            addFace(data['personId'],imageURL)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))



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

  
        print(response.reason)
        print(data)
        #print(response)

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def deletePerson(person):
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
        print("[Errno {0}] {1}".format(e.errno, e.strerror))



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