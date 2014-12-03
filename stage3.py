#!/usr/bin/python
'''
Stage III: Prefix
================================

In this challenge, the API is going to give you another dictionary. The first value, prefix, is a string. 
The second value, array, is an array of strings. Your job is to return an array containing only the 
strings that do not start with that prefix.

Same methodology as stage II. 
When I uploaded the values given to me by the api python reads the values as unicode. In order to use the method starts with
I had to change all of preList values into strings. I did another loop in order to remove the word that had the prefix. But the if
statment executes one time. In order to prompt the program to continue search for other words that had the prefix I used the keyword continue.
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
