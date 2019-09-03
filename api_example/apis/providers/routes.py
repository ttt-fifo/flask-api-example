"""
Routes and views for current endpoint
"""
from flask_restplus import Resource
from core.lib.validators import validate_with
from .namespaces import api
from . import models
from . import validators
from .marshallers import provider_get_marsh
from .marshallers import provider_edit_marsh

provider_mod = models.Provider()
provider_val = validators.Provider()


@api.route("/")
class ProviderList(Resource):

    @api.marshal_list_with(provider_get_marsh)
    def get(self):
        """
        Returns the list of providers
        """
        return provider_mod.all()

    @api.expect(provider_edit_marsh, validate=True)
    @api.marshal_with(provider_get_marsh)
    @validate_with(api, provider_val)
    def post(self):
        """
        Adds a new provider to the list
        """
        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phone'],
                api.payload['language'],
                api.payload['currency'])
        id = provider_mod.insert(args)
        api.payload['id'] = id
        return api.payload


@api.route("/<int:id>")
class Provider(Resource):

    @api.marshal_with(provider_get_marsh)
    def get(self, id):
        """
        Displays the provider detail
        """
        return provider_mod.one(id)

    @api.expect(provider_edit_marsh, validate=True)
    @api.marshal_with(provider_get_marsh)
    @validate_with(api, provider_val)
    def put(self, id):
        """
        Edits the selected provider
        """
        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phone'],
                api.payload['language'],
                api.payload['currency'],
                id)
        provider_mod.update(args)
        api.payload['id'] = id
        return api.payload
