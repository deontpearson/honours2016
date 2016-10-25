from flask import Flask # imports the flask module to use in this app
from flask import render_template

def wordPressAdminHandler(request):
    return render_template('wp-admin.php')
