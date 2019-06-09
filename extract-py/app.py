from flask import Flask

'''Flask instance to create web server'''
app = Flask(__name__)


@app.route('/')
def index():
    return 'TFG index view'
