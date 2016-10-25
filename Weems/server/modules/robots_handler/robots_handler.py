from flask import send_from_directory
import os, sys

dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
def robotsHandler(request):
    return send_from_directory(dir + '/static', request.path[1:])
