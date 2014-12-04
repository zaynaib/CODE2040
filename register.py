'''
   Reference: http://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1
'''
response =requests.get("http://challenge.code2040.org/api/register")
info = {'email':'XXXXXXXXXXXXXX.edu', 'github':'https://github.com/zaynaib/'}
body= json.dumps(info)
token = requests.post('http://challenge.code2040.org/api/register', data=body)
token.text
