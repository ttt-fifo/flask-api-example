from application import api
from flask_restplus import fields


provider_fields = dict(
    name=fields.String(required=True, min_length=1, max_length=200,
                       description='Provider Name'),
    email=fields.String(required=True,
                        example='email@mydomain.com',
                        pattern=r'\S+@\S+\.\S+',
                        description='Provider e-mail'),
    phone=fields.String(required=True, description='Phone Number'),
    language=fields.String(required=True,
                           example='EN',
                           min_length=2,
                           max_length=3,
                           description='Language, choose one from'
                                       ' language list'),
    currency=fields.String())

provider_edit_marsh = api.model('ProviderEdit', provider_fields)

provider_get_marsh = api.clone('ProviderGet', provider_edit_marsh,
                               dict(id=fields.Integer(description='Id')))
