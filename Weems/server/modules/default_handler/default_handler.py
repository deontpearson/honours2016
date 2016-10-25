from flask import Flask # imports the flask module to use in this app
from flask import render_template
from modules.resources import save_file
from werkzeug import secure_filename # to handle file uploads

def defaultHandler(request):
    if request.method == 'POST' and bool(request.files):
        save_file.saveFileToDisk(secure_filename(request.files['file'].filename), request.files['file'].read())
    return render_template('default.html', path=request.path)
