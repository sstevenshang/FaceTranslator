# import cognitive_face as CF
# KEY = '3ba9669a88a84642b96fe901851e988e'
# CF.Key.set(KEY)

# #img_url='https://www.facebook.com/photo.php?fbid=1050128121773175&l=9fceb293d7'
# img_url='https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
# result = CF.face.detect(img_url)
# print(result)



########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers.
    'Content-Type': 'application/json',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '3ba9669a88a84642b96fe901851e988e',
}

# Replace 'examplegroupid' with an ID you haven't used for creating a group before.
# The valid characters for the ID include numbers, English letters in lower case, '-' and '_'. 
# The maximum length of the ID is 64.
personGroupId = 'firstgroupid'

# The userData field is optional. The size limit for it is 16KB.
body = "{ 'name':'group1', 'userData':'user-provided data attached to the person group' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
    #   URL below with "westus".
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/firstgroupid/persons/", body, headers)
    response = conn.getresponse()

    # 'OK' indicates success. 'Conflict' means a group with this ID already exists.
    # If you get 'Conflict', change the value of personGroupId above and try again.
    # If you get 'Access Denied', verify the validity of the subscription key above and try again.
    print(response.reason)
    print(body)

    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################
