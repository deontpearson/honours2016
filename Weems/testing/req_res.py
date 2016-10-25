import requests

getPassed = True
postPassed = True
f = {'file': open('/tmp/test.txt')}
urls = [
'http://146.231.123.9/',
'http://146.231.123.9/foo',
'http://146.231.123.9/foo/bar',
'http://146.231.123.9/foo bar is what',
'http://146.231.123.9/foo/bar/dsada',
'http://146.231.123.9/foo/bar/fdsfsfs/fdsafds/g/sag',
'http://146.231.123.9/foo/bar/index.html',
'http://146.231.123.9/foo.txt',
'http://146.231.123.9/bar.jpg',
'http://146.231.123.9/www.example.com',
]

for a in urls:
    getRes = requests.get(a)
    if getRes.status_code != 200:
        getPassed = False

for b in urls:
    postRes = requests.post(b, files=f)
    if postRes.status_code != 200:
        postPassed = False

print 'GET passed: %r\nPOST passed: %r' % (postPassed, getPassed)
