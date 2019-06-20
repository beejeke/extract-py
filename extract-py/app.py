from flask import Flask, render_template

'''Flask instance to create web server'''
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/patients/')
def patients():
    return render_template('patients.html')
