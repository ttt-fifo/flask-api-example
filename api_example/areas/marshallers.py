from app import api
from flask_restplus import fields
from copy import deepcopy

area_fields = dict(
    id=fields.Integer(description='Id'),
    name=fields.String(required=True, min_length=1, max_length=200,
                       description='Provider Name'),
    price=fields.Float(),
    geom=fields.String())


class Area:

    def __init__(self):
        self.get = api.model('AreaGet', area_fields)

        area_fields_edit = deepcopy(area_fields)
        del area_fields_edit['id']
        self.edit = api.model('AreaEdit',
                              area_fields_edit)
