from flask import Flask # imports the flask module to use in this app
from flask import request # allows us to see the request headers
from flask import render_template
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__, static_url_path='') # creates an instance of the Flask class and calls it app

@app.route('/') # defines what must be done when a request comes in for "/"
def index():
    print (request.method)
    return "home page", 200 #app.send_static_file('index.html'), 200 # returns the text Hello Flask and the response code 200
@app.route("/index")
def adminPage():
    return "index page", 200
@app.route("/wp-admin")
def wordPressAdmin():
    return "word press admin page", 200
if __name__ == "__main__": # __name__ is the name attirbute of the objects
<<<<<<< HEAD
    app.debug = True # enable debugging so that code can be changed without restarting the server
    app.run(host="146.231.123.9", port=8080)
    logger = logging.getLogger('wekzeug') # gets the underlying WSGI logger
    handler = logging.FileHandler('requests.log')
    logger.addHandler(handler) # adds the handler instance to the logger
    app.logger.addhandler(handler)
=======
    app.debug = False # enable debugging so that code can be changed without restarting the server
    #log = logging.getLogger('werkzeug')
    #log.setLevel(logging.ERROR)
    #app.logger.addHandler(handler)
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    app.run(host="127.0.0.1", port=8080)
>>>>>>> master
