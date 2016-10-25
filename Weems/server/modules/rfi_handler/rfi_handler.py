from flask import Flask # imports the flask module to use in this app
from flask import render_template
import re, urllib2
from modules.resources import save_file

r_list = [re.compile(r'http://(.*)'),
re.compile(r'ftp://(.*)'),
re.compile(r'https://(.*)'),
]

def rfiHandler(request):
    for item in request.args:
        for r in r_list:
            if re.match(r, request.args.get(item)):
                try:
                    response = urllib2.urlopen(request.args.get(item))
                    html = response.read()
                    save_file.saveFileToDisk(request.args.get(item), html)
                except:
                    print 'got error'
                    pass
                return render_template('404.html', path=request.args.get(item))
    return render_template('404.html', path=''), 404
