from flask import (Blueprint, flash, jsonify, render_template, redirect, url_for, logging, request)

from extract.model import CamdexData, Patient, User, Variable, db
from extract.schema import PatientInfo, CamdexDataInfo

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

        mmse_new = request.form['mmse_new']
        mec_new = request.form['mec_new']
        roth_new = request.form['roth_new']
        camcog_new = request.form['camcog_new']
        orientacion_new = request.form['orientacion_new']
        lengt_new = request.form['lengt_new']
        lengcom_new = request.form['lengcom_new']
        lengprod_new = request.form['lengprod_new']
        memt_new = request.form['memt_new']
        memrec_new = request.form['memrec_new']
        memrem_new = request.form['memrem_new']
        memapr_new = request.form['memapr_new']
        atencon_new = request.form['atencon_new']
        prax_new = request.form['prax_new']
        calc_new = request.form['calc_new']
        pensabs_new = request.form['pensabs_new']
        percep_new = request.form['percep_new']

        new_patient = Patient(name=name_new,
                              address=address_new,
                              phone=phone_new,
                              email=email_new,
                              age=age_new,
                              dni=dni_new,
                              birthdate=birthdate_new)
        db.session.add(new_patient)
        db.session.commit()

        new_camdex = CamdexData(patient_name=name_new,
                                mmse=mmse_new,
                                mec=mec_new,
                                ryh=roth_new,
                                ct=camcog_new,
                                ori=orientacion_new,
                                lt=lengt_new,
                                lc=lengcom_new,
                                lp=lengprod_new,
                                mt=memt_new,
                                mrec=memrec_new,
                                mrem=memrem_new,
                                ma=memapr_new,
                                ac=atencon_new,
                                pr=prax_new,
                                cal=calc_new,
                                pabs=pensabs_new,
                                ptv=percep_new)

        db.session.add(new_camdex)
        db.session.commit()

        flash('Historial clínico de paciente añadido satisfactoriamente.', 'success')

        print(name_new)
        return redirect(url_for("frontend.patients"))
    return redirect(url_for("frontend.patients"))


@frontend.route('/delete_patient/<name>', methods=["POST"])
def delete_patient(name):
    if request.method == 'POST':
        Patient.query.filter(Patient.name == name).delete()
        CamdexData.query.filter(CamdexData.patient_name == name).delete()
        db.session.commit()

        flash('Historial clínico de paciente eliminado satisfactoriamente.', 'warning')

    return redirect(url_for("frontend.patients"))


@frontend.route("/patients/<name>")
def get_data(name):
    query = Patient.query.filter(Patient.name == name)
    patient_schema = PatientInfo(many=True)
    info = patient_schema.dump(query).data
    return jsonify({'data': info})


@frontend.route("/camdex/<name_p>")
def get_camdex_data(name_p):
    query = CamdexData.query.filter(CamdexData.patient_name == name_p)
    camdex_schema = CamdexDataInfo(many=True)
    camdex = camdex_schema.dump(query).data
    return jsonify({'data': camdex})