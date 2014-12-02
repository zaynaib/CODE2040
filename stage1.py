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
reverseWord = theword[::-1]
key1={"string": reverseWord, "token":"24DVHp6MNU"}
key=json.dumps(key1)
reversePost2 = requests.post('http://challenge.code2040.org/api/validatestring ', data=key)
reversePost2.text
