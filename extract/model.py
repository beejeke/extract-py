# Database model from SQL Alchemy
from datetime import datetime

from enum import Enum


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Variable(Enum):
    MMSE = 1
    MEC = 2
    RYH = 3
    CT = 4
    ORI = 5
    LT = 6
    LC = 7
    LP = 8
    MT = 9
    MREC = 10
    MREM = 11
    MA = 12
    AC = 13
    PR = 14
    CAL = 15
    PABS = 16
    PTV = 17

    @property
    def name_es(self):
        name = {
            self.MMSE: "Mini Mental State de Folstein",
            self.MEC: "Mini Examen Cognoscitivo de Lobo y colbs",
            self.RYH: "Test de Atención-Memoria-Concentración de Roth y Hopkins",
            self.CT: "Camcog total",
            self.ORI: "Orientación",
            self.LT: "Lenguaje total",
            self.LC: "Lenguaje comprensivo",
            self.LP: "Lenguaje productivo",
            self.MT: "Memoria total",
            self.MREC: "Memoria reciente",
            self.MREM: "Memoria remota",
            self.MA: "Memoria aprendizaje",
            self.AC: "Atención-concentración",
            self.PR: "Praxis",
            self.CAL: "Cálculo",
            self.PABS: "Pensamiento abstracto",
            self.PTV: "Percepción táctil-visual"
        }
        return name[self]


"""
Table with Clínica Neurológica Alayón users information
"""


class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(8), nullable=False)


"""
Table with patients personal information
"""


class Patient(db.Model):
    __tablename__ = "patient"
    name = db.Column(db.String(40), primary_key=True)
    address = db.Column(db.String(60), unique=False)
    phone = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer, unique=False)
    dni = db.Column(db.String(9), unique=True)
    birthdate = db.Column(db.String(10))


"""
Table with patients CAMDEX data
"""


class CamdexData(db.Model):
    __tablename__ = "camdex_data"
    patient_name = db.Column(
        db.String(40), db.ForeignKey("patient.name"), primary_key=True
    )
    mmse = db.Column(db.String(40), unique=False, nullable=True)
    mec = db.Column(db.String(40), unique=False, nullable=True)
    ryh = db.Column(db.String(40), unique=False, nullable=True)
    ct = db.Column(db.String(40), unique=False, nullable=True)
    ori = db.Column(db.String(40), unique=False, nullable=True)
    lt = db.Column(db.String(40), unique=False, nullable=True)
    lc = db.Column(db.String(40), unique=False, nullable=True)
    lp = db.Column(db.String(40), unique=False, nullable=True)
    mt = db.Column(db.String(40), unique=False, nullable=True)
    mrec = db.Column(db.String(40), unique=False, nullable=True)
    mrem = db.Column(db.String(40), unique=False, nullable=True)
    ma = db.Column(db.String(40), unique=False, nullable=True)
    ac = db.Column(db.String(40), unique=False, nullable=True)
    pr = db.Column(db.String(40), unique=False, nullable=True)
    cal = db.Column(db.String(40), unique=False, nullable=True)
    pabs = db.Column(db.String(40), unique=False, nullable=True)
    ptv = db.Column(db.String(40), unique=False, nullable=True)