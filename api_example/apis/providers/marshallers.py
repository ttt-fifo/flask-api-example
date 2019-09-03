from .namespaces import api
from flask_restplus import fields

provider_fields = {}
provider_fields['id'] = fields.Integer()
provider_fields['name'] = fields.String(required=True,
                                        min_length=1, max_length=200,
                                        description='Provider Name')
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

provider_marsh = api.model('Provider', provider_fields)
