from api import ma
from ..models import equipamento_model
from marshmallow import fields


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = employee_model.Employee
        fields = ("id", "name", "age", "projects")

    name = fields.String(required=True)
    age = fields.String(required=True)
