#------------------------------------------------------------------------------------#
#-------------------------------REQUIRED MODULES-------------------------------------#
#------------------------------------------------------------------------------------#
# pip install jinja2 > for templating
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
# usefull info drom other modules
# request logger args = {
#   'pid':primaryID,
#   'src': soruceAddress,
#   'date':datetime,
#   'method':method,
#   'resource': resource,
#   'http': httpVersion,
#   'code': responseCode
# }

from flask import Flask # imports the flask module to use in this app
from flask import request # allows us to see the request headers
# Custom modules for my honeypot
from modules.logger import my_logger
from modules.handler import my_handler

SPECIAL_PAGES = ['stats', 'requests']

app = Flask(__name__) # creates an instance of the Flask class and calls it app

# With these routes setup we are catching *any* possible URL/request.
# The root URL/domain for the app (/) is catched by the first route
# While the second route using the path placeholder will catch any
# route like /login, /logout, or even /foo/bar.
@app.route('/', defaults={'path':'/'}) # defines what must be done when a request comes in for "/"
@app.route('/<path:path>')
def catchAll(path):
    if path not in SPECIAL_PAGES:
        my_logger.logRequest(log, {'src': request.remote_addr, 'method': request.method, 'resource': request.path, 'http': 'HTTP1/1', 'code': 200}) # logs every request that comes into the server
    pathOptions = {'/':my_handler.rootHandler,
                    'wp-admin':my_handler.wordPressAdminHandler,
                    'stats': my_handler.displayStats,
                    'requests' :  my_handler.displayRequestsInfo
                    }

    if path in SPECIAL_PAGES and not request.remote_addr == '146.231.123.9': # special path
        return my_handler.noHandler(), 203
    elif path in pathOptions: # handle any implemented modules
        return pathOptions[path](), 200
    else: # handle any paths not implemented
        return my_handler.noHandler(path), 203

if __name__ == "__main__": # __name__ is the name attirbute of the objects
    log = my_logger.getMyLogger('request_logger') # creates a new log object to write logs to
    app.run(host="146.231.123.9", port=8080,debug=True)
