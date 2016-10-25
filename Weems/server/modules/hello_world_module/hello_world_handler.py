from flask import Flask # imports the flask module to use in this app
from flask import render_template


def helloWorldHandler(request):
    return render_template('helloworld.html', input="hello world"), 418
