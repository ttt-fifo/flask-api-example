from app import api
from flask_restplus import fields
from copy import deepcopy

provider_fields = dict(
    id=fields.Integer(description='Id'),
    name=fields.String(required=True, min_length=1, max_length=200,
                       description='Provider Name'),
    email=fields.String(),
    phonenumber=fields.String(),
    language=fields.String(),
    currency=fields.String())


class Provider:

    def __init__(self):
        self.get = api.model('ProviderGet', provider_fields)

        provider_fields_add = deepcopy(provider_fields)
        del provider_fields_add['id']
        self.edit = api.model('ProviderEdit',
                              provider_fields_add)
