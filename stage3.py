'''
Stage III: Prefix
================================

In this challenge, the API is going to give you another dictionary. The first value, prefix, is a string. 
The second value, array, is an array of strings. Your job is to return an array containing only the 
strings that do not start with that prefix.

'''

import requests
import json


url = 'http://challenge.code2040.org/api/prefix'
data = '{"token": "24DVHp6MNU"}'
preFixRequests=requests.post(url, data=data)
values = json.loads(preFixRequests.text)
preList = values["result"].get("array") 
preWord = str(values["result"].get("prefix"))


for i in range (0, len(preList)):
    preList[i] = str(preList[i])

for word in preList:
    if word.startswith(preWord):
	    preList.remove(word)
    continue
	

key1={"array": preList, "token":"24DVHp6MNU"}
key=json.dumps(key1)
reversePost2 = requests.post('http://challenge.code2040.org/api/validateprefix', data=key)
reversePost2.text	
