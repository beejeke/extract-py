from flask import Blueprint, jsonify, render_template

from extract.model import CamdexData, Patient, User, Variable, db
from extract.schema import PatientInfo

frontend = Blueprint('frontend', __name__, url_prefix='/')


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/patients/')
def patients():
    patient = Patient.query.order_by(Patient.name).all()
    return render_template('patients.html', patient=patient)


@frontend.route("/patients/<name>")
def get_data(name):
    query = Patient.query.filter(Patient.name == name)
    patient_schema = PatientInfo(many=True)
    info = patient_schema.dump(query).data
    return jsonify({'data': info})