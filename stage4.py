'''
Stage IV: The dating game
================================

The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp.
The value for interval is a number of seconds.

This challenge was very tricky for me. I have rarely experimented with dates in programming. This is my first time doing it in
python. I retreive the values turn them into strings. For datestamp I converted to seconds in order to make it easier for me
to add time. I cast datestamp and interval information as intergers in order to add them.  Changed the seconds into
at datestamp and tried to formatit in isoformat. I tried figuring out formatting the mircoseconds. Still working on it.
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
