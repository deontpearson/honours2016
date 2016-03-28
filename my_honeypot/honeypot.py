# terminal commands needed for this server


from flask import Flask # imports the flask module to use in this app
from flask import request # allows us to see the request headers
from flask import render_template
import logging # to use the standard pyton logger
import logging.config # to use a config file for logging


app = Flask(__name__, static_url_path='') # creates an instance of the Flask class and calls it app

@app.route('/') # defines what must be done when a request comes in for "/"
def index():
    log.info('%(method)s pid:%(pid)d' % {'method':request.method, 'pid':100})
    return "home page", 200 #app.send_static_file('index.html'), 200 # returns the text Hello Flask and the response code 200
@app.route("/index")
def adminPage():
    return "index page", 200
@app.route("/wp-admin")
def wordPressAdmin():
    return "word press admin page", 200
if __name__ == "__main__": # __name__ is the name attirbute of the objects
    #app.debug = True # enable debugging so that code can be changed without restarting the server

    logging.config.fileConfig('logging.conf') # uses an external logging file to get configuration information
    log = logging.getLogger('request_logger') # sets log to be the request logger from the logging.conf file

    app.run(host="127.0.0.1", port=8080)
