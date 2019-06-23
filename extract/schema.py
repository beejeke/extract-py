from marshmallow_sqlalchemy import ModelSchema
from extract.model import Patient


class PatientInfo(ModelSchema):
    class Meta:
        model = Patient