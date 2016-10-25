from flask import Flask # imports the flask module to use in this app
from flask import render_template
from modules.resources import save_file

def fileUploadHandler(request):
    "This function processes the GET request for /upload"
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        save_file.saveFileToDisk(secure_filename(request.files['file'].filename), request.files['file'].read()) # file storage object containing the file)
        return 'file uploaded successfully'
