from flask import Flask # imports the flask module to use in this app
from flask import render_template

def displayStats(): # called using md5 has of statspage
    "retrievs stats from a file name stats.info"
    stats = ''
    tempList = open('./data/stats.info', 'r').read().split('\n')
    for i in tempList:
        if i != '':
            stats += '%s<br>' % i
    return stats

def displayRequestsInfo(): # called using md5 has of acceslogs
    "retrievs request from access logs"
    stats = ''
    tempList = open('./logs/access.log', 'r').read().split('\n')
    for i in tempList:
        if i != '':
            stats += '%s<br>' % i
    return stats
def rootHandler():
    return render_template('index.html')
def wordPressAdminHandler():
    return render_template('admin.html')
def noHandler(path):
    return render_template('default.html', path=path)
