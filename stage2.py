'''
Stage II: Needle in a haystack
================================

Next, let’s check your skills for working with collections.

We’re going to send you a dictionary with two values and keys. The first value, needle, is a string.
The second value, haystack, is an array of strings. You’re going to tell the API where the needle is in the array.

'''

import requests
import json

url = 'http://challenge.code2040.org/api/haystack'
data = '{"token": "24DVHp6MNU"}'
needleRequests=requests.post(url, data=data)
hay = json.loads(needleRequests.text)
stack = hay["result"].get("haystack") 
needle = str(hay["result"].get("needle"))
needleLoca =0
for s in stack:
    if needle in str(s):
        needleLoca = stack.index(s)
		
key1={"needle": needleLoca, "token":"24DVHp6MNU"}
key=json.dumps(key1)
reversePost2 = requests.post('http://challenge.code2040.org/api/validateneedle', data=key)
reversePost2.text
