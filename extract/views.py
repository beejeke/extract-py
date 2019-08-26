import json
import plotly
import plotly.graph_objs as go

from flask import (Blueprint, flash, jsonify, render_template, redirect, url_for, logging, request)

from extract.model import CamdexData, Patient, User, Variable, db
from extract.schema import PatientInfo, CamdexDataInfo
from extract.chart import data_graphs

frontend = Blueprint('frontend', __name__, url_prefix='/')


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/charts')
def charts():
    patient = Patient.query.order_by(Patient.name).all()
    return render_template('charts.html', patient=patient)


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


@frontend.route('/edit_patient/<string:name>')
def edit_patient(name):
    patient = Patient.query.filter(Patient.name == name).first()
    camdex = CamdexData.query.filter(CamdexData.patient_name == name).first()

    return render_template('edit.html', patient=patient, camdex=camdex)


@frontend.route('/update_patient/<string:name>', methods=['POST'])
def update_patient(name):
    if request.method == 'POST':
        address_mod = request.form['address_mod']
        phone_mod = request.form['phone_mod']
        email_mod = request.form['email_mod']
        age_mod = request.form['age_mod']
        dni_mod = request.form['dni_mod']
        birthdate_mod = request.form['birthdate_mod']

        mmse_mod = request.form['mmse_mod']
        mec_mod = request.form['mec_mod']
        ryh_mod = request.form['ryh_mod']
        camcog_mod = request.form['ct_mod']
        orientacion_mod = request.form['ori_mod']
        lengt_mod = request.form['lt_mod']
        lengcom_mod = request.form['lc_mod']
        lengprod_mod = request.form['lp_mod']
        memt_mod = request.form['mt_mod']
        memrec_mod = request.form['mrec_mod']
        memrem_mod = request.form['mrem_mod']
        memapr_mod = request.form['ma_mod']
        atencon_mod = request.form['ac_mod']
        prax_mod = request.form['pr_mod']
        calc_mod = request.form['cal_mod']
        pensabs_mod = request.form['pabs_mod']
        percep_mod = request.form['ptv_mod']

        updated_patient = Patient.query.filter(Patient.name == name).first()
        updated_camdex = CamdexData.query.filter(CamdexData.patient_name == name).first()

        updated_patient.address = address_mod
        updated_patient.phone = phone_mod
        updated_patient.email = email_mod
        updated_patient.age = age_mod
        updated_patient.dni = dni_mod
        updated_patient.birthdate = birthdate_mod

        db.session.commit()

        updated_camdex.mmse = mmse_mod
        updated_camdex.mec = mec_mod
        updated_camdex.ryh = ryh_mod
        updated_camdex.ct = camcog_mod
        updated_camdex.ori = orientacion_mod
        updated_camdex.lt = lengt_mod
        updated_camdex.lc = lengcom_mod
        updated_camdex.lp = lengprod_mod
        updated_camdex.mt = memt_mod
        updated_camdex.mrec = memrec_mod
        updated_camdex.mrem = memrem_mod
        updated_camdex.ma = memapr_mod
        updated_camdex.ac = atencon_mod
        updated_camdex.pr = prax_mod
        updated_camdex.cal = calc_mod
        updated_camdex.pabs = pensabs_mod
        updated_camdex.ptv = percep_mod

        db.session.commit()

        flash('Historial clínico de paciente modificado satisfactoriamente.', 'info')

        return redirect(url_for("frontend.patients"))
    return redirect(url_for("frontend.patients"))


@frontend.route('/delete_patient/<string:name>')
def delete_patient(name):
    patient = Patient.query.filter(Patient.name == name).first()
    camdex = CamdexData.query.filter(CamdexData.patient_name == name).first()

    db.session.delete(patient)
    db.session.delete(camdex)
    db.session.commit()

    flash('Historial clínico de paciente eliminado satisfactoriamente.', 'warning')

    return redirect(url_for("frontend.patients", patient=patient))


@frontend.route("/chart/<name>/<chart_name>")
def split_data(name, chart_name):
    camdex_mmse = CamdexData.query.filter(CamdexData.patient_name == name).all()

    for row in camdex_mmse:
        if chart_name == 'mmse':
            mmse_x = [1, 2, 3, 4]
            mmse_y = [yaxis.strip() for yaxis in row.mmse.split(',')]
            mmse_y.reverse()

            data_ = data_graphs[CamdexData.mmse](mmse_x, mmse_y)

            return jsonify(data_)

        elif chart_name == 'mec':
            mec_x = [1, 2, 3, 4]
            mec_y = [yaxis.strip() for yaxis in row.mec.split(',')]
            mec_y.reverse()

            data_ = data_graphs[CamdexData.mec](mec_x, mec_y)

            return jsonify(data_)

        elif chart_name == 'ryh':
            ryh_x = [1, 2, 3, 4]
            ryh_y = [yaxis.strip() for yaxis in row.ryh.split(',')]
            ryh_y.reverse()

            data_ = data_graphs[CamdexData.ryh](ryh_x, ryh_y)

            return jsonify(data_)


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