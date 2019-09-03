from .namespaces import api
from flask_restplus import fields
from copy import deepcopy

# nested provider marshaller
provider_fields = {}
provider_fields['id'] = fields.Integer(description='Provider id',
                                       example=14)
provider_fields['name'] = fields.String(description='Provider Name',
                                        example='Snakeoil Ltd')
provider_fields['uri'] = fields.Url('providers_provider')
provider_marsh = api.model('AreaProvider', provider_fields)

# area get marshaller
area_fields = {}
area_fields['id'] = fields.Integer(required=True,
                                   description='Area id',
                                   example=14)
area_fields['name'] = fields.String(required=True,
                                    description='Area Name',
                                    example='Tele District')
area_fields['price'] = fields.Float(required=True,
                                    description='Area Price',
                                    example=10.54)
area_fields['geom'] = fields.String(required=True,
                                    description='Area Geometry',
                                    example='POLYGON ((11 50,11 51,'
                                            '12 51,12 50,11 50))')
area_fields['provider'] = fields.Nested(provider_marsh)
area_get_marsh = api.model('AreaGet', area_fields)

# area edit marshaller
area_edit_fields = deepcopy(area_fields)
del area_edit_fields['id']
del area_edit_fields['provider']
area_edit_fields['provider'] = fields.Integer(required=True,
                                              description='Provider id',
                                              example=14)
area_edit_marsh = api.model('AreaEdit', area_edit_fields)
