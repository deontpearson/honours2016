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
from flask import render_template


# Custom modules for my honeypot
from modules.logger import my_logger

app = Flask(__name__, static_url_path='') # creates an instance of the Flask class and calls it app

@app.route('/') # defines what must be done when a request comes in for "/"
def index():
    my_logger.logRequest(log, {'pid':1, 'src': request.remote_addr, 'method': request.method, 'resource': request.url, 'http': 'HTTP1/1', 'code': 200})
    return "home page", 200 #app.send_static_file('index.html'), 200 # returns the text Hello Flask and the response code 200
@app.route("/index")
def adminPage():
    return "index page", 200
@app.route("/wp-admin")
def wordPressAdmin():
    return "word press admin page", 200
if __name__ == "__main__": # __name__ is the name attirbute of the objects
    #app.debug = True # enable debugging so that code can be changed without restarting the server
    log = my_logger.getMyLogger() # creates a new log object to write logs to
    app.run(host="127.0.0.1", port=8080)
