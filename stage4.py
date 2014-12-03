'''
Stage IV: The dating game
================================

The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp.
The value for interval is a number of seconds.

This challenge was very tricky for me. I have rarely experimented with dates in programming. I refered to this python wiki article on working with time: https://wiki.python.org/moin/WorkingWithTime. I retreive the values turn them into strings. For datestamp I converted to seconds in order to make it easier for me
I cast d.atestamp and interval information as intergers in order to add them.  Next I changed the seconds into isoformat.
'''
import requests
import json
from datetime import datetime
from datetime import datetime, timedelta

url = 'http://challenge.code2040.org/api/time'
data = '{"token": "24DVHp6MNU"}'
timeRequests=requests.post(url, data=data)
values = json.loads(timeRequests.text)
datestamp= str( values["result"].get("datestamp") )
interval =  str(values["result"].get("interval"))

# strptime() parses a string representing a time according to a format
utc_dt = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
# convert UTC datetime to seconds since the Epoch -point where time starts 1/1/1970

timestamp = (utc_dt - datetime(1970, 1, 1)).total_seconds()



timestamp1= float(timestamp) + float(interval)
dt1 = datetime(1970, 1, 1) + timedelta(seconds=timestamp1)

finalT =dt1.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
key1={"datestamp": finalT, "token":"24DVHp6MNU"}
key=json.dumps(key1)
reversePost2 = requests.post('http://challenge.code2040.org/api/validatetime', data=key)
reversePost2.text	
