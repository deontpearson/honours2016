from flask import Flask # imports the flask module to use in this app
from flask import request # allows us to see the request headers
from flask import render_template
app = Flask(__name__, static_url_path='') # creates an instance of the Flask class and calls it app

@app.route('/') # defines what must be done when a request comes in for "/"
def index():
    return "home page", 200 #app.send_static_file('index.html'), 200 # returns the text Hello Flask and the response code 200
@app.route("/index")
def adminPage():
    return render_template('index.html')
if __name__ == "__main__": # __name__ is the name attirbute of the objects
    app.debug = True # enable debugging so that code can be changed without restarting the server
    app.run(host="146.231.123.9", port=8080)
