'''
Stage IV: The dating game
================================

The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp.
The value for interval is a number of seconds.
'''

import dateutil.parser as dp
import datetime
import requests
import json
url = 'http://challenge.code2040.org/api/time'
data = '{"token": "24DVHp6MNU"}'
timeRequests=requests.post(url, data=data)
values = json.loads(timeRequests.text)
datestamp= str( values["result"].get("datestamp") )
interval =  str(values["result"].get("interval"))
t = datestamp
parsed_t = dp.parse(t)
t_in_seconds = parsed_t.strftime('%s')
t_in_seconds
totalTime = int(t_in_seconds )+ int(interval)
myTime = datetime.datetime.fromtimestamp(totalTime).isoformat()
key1={"datestamp": myTime, "token":"24DVHp6MNU"}
key=json.dumps(key1)
reversePost2 = requests.post('http://challenge.code2040.org/api/validatetime', data=key)
reversePost2.text	
