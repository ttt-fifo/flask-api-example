from .namespaces import api
from flask_restplus import fields

area_fields = dict(
    name=fields.String(required=True, min_length=1, max_length=200,
                       description='Area Name'),
    price=fields.Float(required=True, description='Price in this Area'),
    geom=fields.String(required=True,
                       description='Area Geometry',
                       example='POLYGON ((11 50,11 51,12 51))'))

area_edit_marsh = api.model('AreaEdit', area_fields)
area_get_marsh = api.clone('AreaGet', area_edit_marsh,
                           dict(id=fields.Integer(description='id')))
