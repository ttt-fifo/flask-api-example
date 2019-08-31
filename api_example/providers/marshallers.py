from app import api
from flask_restplus import fields
from app import custom_fields
from copy import deepcopy


provider_fields = dict(
    id=fields.Integer(description='Id'),
    name=fields.String(required=True, min_length=1, max_length=200,
                       description='Provider Name'),
    email=custom_fields.Email(required=True, description='Provider e-mail'),
    phone=fields.String(required=True, description='Phone Number'),
    language=custom_fields.Language(required=True,
                                    description='Language'),
    currency=fields.String())


class Provider:

    def __init__(self):
        self.get = api.model('ProviderGet', provider_fields)

        provider_fields_edit = deepcopy(provider_fields)
        del provider_fields_edit['id']
        self.edit = api.model('ProviderEdit',
                              provider_fields_edit)

    def validate_edit(self, payload):
        self.edit['email'].validate(payload['email'])
        self.edit['language'].validate(payload['language'])
