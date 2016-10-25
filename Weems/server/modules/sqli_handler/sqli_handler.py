from flask import Flask # imports the flask module to use in this app
from flask import render_template
import os, sys

dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]

def logPostRequest(args):
    if not os.path.exists(dir + '/data/logs/sqli'):
        os.makedirs(dir + '/data/logs/sqli')
    with open(dir + '/data/sqli/args.dat', 'a') as f:
            f.write('%s' % (args.get('id')+'\n'),)


def processArgs(args):
    if "'" in args.get('id'):
        logPostRequest(args)
        return 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near  \'\'\'\'\' at line 1'
    else:
        logPostRequest(args)
        return render_template('index.html')

def sqliHandler(request):
    return processArgs(request.args), 500
