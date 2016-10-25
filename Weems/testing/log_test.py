import requests

url = 'http://146.231.123.9/foo/bar'
f = {'file': open('/tmp/test.txt')}

getRes = requests.get(url)
postRes = requests.post(url, files=f)

if getRes.status_code == 200:
    print 'GET Completed'
else:
    print 'GET Failed'

if postRes.status_code == 200:
    print 'POST Completed'
else:
    print 'POST Failed'
