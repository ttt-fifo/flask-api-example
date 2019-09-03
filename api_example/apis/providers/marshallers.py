"""
Marshallers for the current endpoint
"""
from copy import deepcopy
from flask_restplus import fields
from .namespaces import api

# provider marshaller constructoin
provider_fields = {}
provider_fields['id'] = fields.Integer(description='Provider id',
                                       example=14)
provider_fields['name'] = fields.String(required=True,
                                        min_length=1, max_length=200,
                                        description='Provider Name',
                                        example='Snakeoil Ltd')
provider_fields['email'] = fields.String(required=True,
                                         example='email@mydomain.com',
                                         pattern=r'\S+@\S+\.\S+',
                                         description='Provider e-mail')
provider_fields['phone'] = fields.String(required=True,
                                         example='+359888784983',
                                         pattern=r'[\+\d]+',
                                         description='Phone Number')
provider_fields['language'] = fields.String(required=True,
                                            example='EN',
                                            min_length=2,
                                            max_length=3,
                                            description='Language,'
                                            ' choose one from'
                                            ' language list')
provider_fields['currency'] = fields.String(required=True,
                                            example='BGN',
                                            min_length=3,
                                            max_length=3,
                                            description='Currency,'
                                            ' choose one from'
                                            ' currency list')
provider_fields['uri'] = fields.Url('providers_provider',
                                    description='Provider URI')

# construct get marshaller from the fields
provider_get_marsh = api.model('ProviderGet', provider_fields)

# edit marshaller
provider_edit_fields = deepcopy(provider_fields)
del provider_edit_fields['id']
del provider_edit_fields['uri']
provider_edit_marsh = api.model('ProviderEdit', provider_edit_fields)
