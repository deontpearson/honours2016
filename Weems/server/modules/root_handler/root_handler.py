from flask import Flask # imports the flask module to use in this app
from flask import render_template

def rootHandler(request):
    # print request.args.get('page')
    return render_template('index.html')
