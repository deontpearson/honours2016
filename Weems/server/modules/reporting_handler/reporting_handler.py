from flask import Flask # imports the flask module to use in this app
from flask import render_template
import os, sys

FILES = {}

dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]

def returnFile(file): # called using md5 has of acceslogs
    "retrievs request from access logs"
    result = ''
    tempList = open(FILES[file], 'r').read().split('\n')
    for i in tempList:
        if i != '':
            result += '%s<br>' % i
    return result

def reportingHandler(request):
    for dirname, subdirList, fileList in os.walk(dir + '/data'):
        for fname in fileList:
            FILES[fname] = dirname +'/'+ fname
    if not request.args.get('report') == None:
        reportNumber = int(request.args.get('report'))
        if reportNumber < len(FILES):
            return render_template('log.html', title=FILES.keys()[reportNumber], info=returnFile(FILES.keys()[reportNumber]))
        else:
            return 'Report does not exist'
    reports = ''
    for item in (FILES.keys()):
        reports += '%d: %s<br>' % (FILES.keys().index(item), item,)
    return render_template('reports.html', reports=reports)
