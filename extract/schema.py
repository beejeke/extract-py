from marshmallow_sqlalchemy import ModelSchema

from extract.model import CamdexData, Patient


class PatientInfo(ModelSchema):
    class Meta:
        model = Patient


class CamdexDataInfo(ModelSchema):
    class Meta:
        model = CamdexData