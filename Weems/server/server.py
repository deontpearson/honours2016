#-------------------------------REQUIRED MODULES-------------------------------------#
#------------------------------------------------------------------------------------#
# pip install jinja2 > for templating
# apt-get install python-flask > for flask
# pip install pyyaml > yaml
# pip install pytz ? pytz
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#

from flask import Flask # imports the flask module to use in this app
from flask import request # allows us to see the request headers
import os # for os task such as getting the working directory
import logging # to turn off logging to console
import time
import re
import urllib2
from modules.default_logger import default_logger as logger
from modules.default_handler import default_handler as dh
import argparse # https://docs.python.org/2/library/argparse.html#module-argparse
from modules.wp_login_handler import wp_login_handler
from modules.rfi_handler import rfi_handler
from modules.file_upload_handler import file_upload_handler
from modules.hello_world_module import hello_world_handler
from modules.root_handler import root_handler
from modules.sqli_handler import sqli_handler
from modules.robots_handler import robots_handler
from modules.wp_admin_handler import wp_admin_handler
from modules.reporting_handler import reporting_handler


#Globals------------------------------------------
HOST = None
PORT = None
DEBUG = False
SSL = False
ADMIN_IP = '146.231.123.9'
ADMIN_PAGES = ['a62ae1c57d16eedbdba51dbf8a247988/reports',]
PATHS = {'wp-login.php' : (wp_login_handler.wordPressLoginHandler,[r'^wp-login.php',]),'rfi' : (rfi_handler.rfiHandler,[r'(.*)http://(.*)', r'(.*)ftp://(.*)', r'(.*)https://(.*)',]),'upload' : (file_upload_handler.fileUploadHandler,[r'^upload$',]),'helloworld' : (hello_world_handler.helloWorldHandler,[r'^helloworld$',]),'/' : (root_handler.rootHandler,[r'^/$',]),'results.html' : (sqli_handler.sqliHandler,[r'^results.html$',]),'robots.txt' : (robots_handler.robotsHandler,[r'^robots.txt^',]),'wp-admin' : (wp_admin_handler.wordPressAdminHandler,[r'^wp-admin',]),'a62ae1c57d16eedbdba51dbf8a247988/reports' : (reporting_handler.reportingHandler,[r'^a62ae1c57d16eedbdba51dbf8a247988/reports',]),}
#-------------------------------------------------

app = Flask(__name__) # creates an instance of the Flask class and calls it app

# With these routes setup we are catching *any* possible URL/request.
# The root URL/domain for the app (/) is caught by the first route
# While the second route using the path placeholder will catch any
# route like /login, /logout, or even /foo/bar.
# Can handle GET and POST requests
@app.route('/', defaults={'path':'/'}, methods=['GET', 'POST']) # defines what must be done when a request comes in for "/"
@app.route('/<path:path>', methods=['GET', 'POST']) # catch all paths
def handleRequests(path):
    fp = path
    if request.args:
         fp += '?' + request.query_string
    if not request.remote_addr == ADMIN_IP or DEBUG == True: # log all requests that are not made from ADMIN_IP
        logger.loggingHandler(request, HOST, PORT)
    if path in ADMIN_PAGES and not request.remote_addr == ADMIN_IP: # if a request comes for a special page but not from ADMIN_IP call noHandler
        return dh.defaultHandler(request), 200
    for item in PATHS:
        if any(re.compile(r, re.I).match(fp) for r in PATHS[item][1]):
            return PATHS[item][0](request) #return PATHS[path](request)
    else: # handle any paths not implemented
        return dh.defaultHandler(request), 200

if __name__ == "__main__": # __name__ is the name attirbute of the objects
#    clog = default_logger.getLogger('access_logs') # creates a new log object to write logs to in the common log format style
#    rlog = default_logger.getLogger('request_logs') # log file for requests
    # description = a description of what the program does
    parser = argparse.ArgumentParser(description='Creates an instance of the server') # holds all the information to parse the command line
    rg = parser.add_argument_group('required arguments') # creates a required arguments group

    # action = how the command line arguments should be added
    # const = holds a constant value
    #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    #parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    rg.add_argument('-i', dest='ip', default='127.0.0.1', help='The IP to bind the instance to.', required=True)
    rg.add_argument('-p', dest='port', default='8080', type=int, help='The Port to bind the instance to.', required=True)
    parser.add_argument('-s', dest='ssl', action='store_const', const=True, help='Turns SSL on.')
    parser.add_argument('-d', dest='debug', action='store_const', const=True, help='Sets the debug flag on') # this is a flag type usage, if -d is seen it stores the constant value True to the namespace
    args = parser.parse_args() # gets the args supplied to it
    HOST = args.ip # assigns the ip args to HOST
    DEBUG = args.debug
    PORT = args.port
    SSL = args.ssl
    #elog = default_logger.getLogger('error_log', 'error.log') # log errors that occur
    #app.logger.addHandler(elog)
    if not DEBUG:
        time.sleep(10) # makes it sleep for 10 secs for crontab service to initiate the network card
    if SSL:
        app.run(host=HOST, port=PORT,debug=DEBUG, ssl_context='adhoc')
    else:
        app.run(host=HOST, port=PORT,debug=DEBUG)
