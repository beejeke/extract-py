from flask import Blueprint, render_template

from extract.model import CamdexData, Patient, User, Variable, db

frontend = Blueprint('frontend', __name__, url_prefix='/')


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/patients/')
def patients():
    return render_template('patients.html')