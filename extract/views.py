from flask import (Blueprint, flash, jsonify, render_template, redirect, url_for, logging, request)

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


@frontend.route('/add_patient', methods=["POST"])
def add_patient():
    if request.method == 'POST':
        name_new = request.form['name_new']
        address_new = request.form['address_new']
        phone_new = request.form['phone_new']
        email_new = request.form['email_new']
        age_new = request.form['age_new']
        dni_new = request.form['dni_new']
        birthdate_new = request.form['birthdate_new']

        new_patient = Patient(name=name_new,
                              address=address_new,
                              phone=phone_new,
                              email=email_new,
                              age=age_new,
                              dni=dni_new,
                              birthdate=birthdate_new)
        db.session.add(new_patient)
        db.session.commit()

        flash('Historial clínico de paciente añadido satisfactoriamente', 'success')

        print(name_new)
        return redirect(url_for("frontend.patients"))
    return redirect(url_for("frontend.patients"))


@frontend.route('/delete_patient/<name>', methods=["POST"])
def delete_patient(name):
    if request.method == 'POST':
        Patient.query.filter(Patient.name == name).delete()
        db.session.commit()

        flash('Historial clínico de paciente eliminado satisfactoriamente', 'warning')

    return redirect(url_for("frontend.patients"))


@frontend.route("/patients/<name>")
def get_data(name):
    query = Patient.query.filter(Patient.name == name)
    patient_schema = PatientInfo(many=True)
    info = patient_schema.dump(query).data
    return jsonify({'data': info})