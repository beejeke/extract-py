from flask import (Blueprint, jsonify, render_template, redirect, url_for, logging, request)

from extract.model import CamdexData, Patient, User, Variable, db
from extract.schema import PatientInfo

frontend = Blueprint('frontend', __name__, url_prefix='/')


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userlog = request.form["userlog"]
        pwdlog = request.form["pwdlog"]

        login = User.query.filter_by(username=userlog, password=pwdlog).first()
        if login is not None:
            return redirect(url_for("frontend.patients"))
    return render_template("login.html")


@frontend.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        userreg = request.form['userreg']
        pwdreg = request.form['pwdreg']

        register = User(username=userreg, password=pwdreg)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("frontend.patients"))
    return render_template("register.html")


@frontend.route('/patients')
def patients():
    patient = Patient.query.order_by(Patient.name).all()
    return render_template('patients.html', patient=patient)


@frontend.route("/patients/<name>")
def get_data(name):
    query = Patient.query.filter(Patient.name == name)
    patient_schema = PatientInfo(many=True)
    info = patient_schema.dump(query).data
    return jsonify({'data': info})