'''
Stage I: Reverse a string
'''

import requests
import json

url = 'http://challenge.code2040.org/api/getstring'
data = '{"token": "24DVHp6MNU"}'
t=requests.post(url, data=data)
word = json.loads(t.text)
theword = str(word["result"])
reverseWord = theword[::-1] #Extended Slice with a stepwise of -1 so it will copy the list in reverse order
key1={"string": reverseWord, "token":"24DVHp6MNU"} #create a dictionary
key=json.dumps(key1) #turn the dictionary to a json object
reversePost2 = requests.post('http://challenge.code2040.org/api/validatestring ', data=key) #send the information to the api
reversePost2.text 
