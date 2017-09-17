########### Python 2.7 #############
import httplib, urllib, base64, json, sys
import setupPersonGroup as spg




headers = {
    # Request headers.
    'Content-Type': 'application/json',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '37e02440a4dd4ef2b738acf9e5dd46ac',
}


# Replace 'examplegroupid' with an ID you haven't used for creating a group before.
# The valid characters for the ID include numbers, English letters in lower case, '-' and '_'. 
# The maximum length of the ID is 64.
personGroupId = 'firstgroupid'

# The userData field is optional. The size limit for it is 16KB.
body = "{ 'name':'group1', 'userData':'user-provided data attached to the person group' }"
#body = "{ 'name': 'campion', 'userData':'so cool' }"








def getFaceId(url):
    try:
        #personId = "10c69ca3-3c4b-427b-b777-a4c8582df20c"
        #body = "{'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/11024678_763791060406884_5211712562033115495_o.jpg?oh=6bce7862e00379a766b697006f86f879&oe=5A44BE3B'}"
        #body = "{'url': 'https://scontent.fzty2-1.fna.fbcdn.net/v/t31.0-8/13244261_939245159506499_4022522226824089791_o.jpg?oh=5aa0f305d66e10116de106e1d2bf447c&oe=5A483B2C'}"
        print("*************")
        print(url)
        #body = "{'url': '" + url + "'}"
        body = "{'url': 'https://raw.githubusercontent.com/sstevenshang/FaceTranslator/master/nodeserver/face4.jpg'}"
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect/", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())

        print("ayo hey")
        print(response.reason)
        print(data[0]['faceId'])
        idFace(data[0]['faceId'])

        #print(response)

        conn.close()
    except Exception as e:
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))



def idFace(faceId):
    #print("in here")
    #print(faceId)
    body = "{'personGroupId':'firstgroupid','faceIds':['" + faceId + "'],'maxNumOfCandidatesReturned':1,'confidenceThreshold': 0.5}"
    try:

        #personId = "10c69ca3-3c4b-427b-b777-a4c8582df20c"
        conn = httplib.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/identify/", body, headers)
        response = conn.getresponse()
        data = json.loads(response.read())


        #print(response.reason)
        #print(data)
        if (len(data[0]['candidates']) == 0):
            print("oh fuck not found")
            #sys.exit(0)
        else:
            #print(data[0]['candidates'][0]['personId'])
            #print(data[0]['candidates'][0]['confidence'])
            
            foundHim = data[0]['candidates'][0]['personId']
            everyone = spg.getEveryone()
            for person in everyone:
                if (foundHim == person['personId']):
                    #print(person['personId'])
                    print(person['name'])

            #print(response)

        conn.close()
    except Exception as e:
        print(e)
        #print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__=="__main__":
    #url = "https://raw.githubusercontent.com/sstevenshang/FaceTranslator/master/steven.jpg"
    url = sys.argv[1]
    print(url)
    getFaceId(url)




