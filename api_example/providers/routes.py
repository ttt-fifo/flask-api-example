from flask_restplus import Resource
from app import api
from . import models as mod
from . import serializers as ser

provider_ns = api.namespace('providers', description='Providers Manipulation')


@provider_ns.route("/")
class ProviderList(Resource):

    @api.marshal_list_with(ser.Provider().get)
    def get(self):
        """
        Returns the list of providers
        """
        return mod.Provider().all()

    @api.expect(ser.Provider().edit, validate=True)
    @api.marshal_with(ser.Provider().get)
    def post(self):
        """
        Adds a new provider to the list
        """
        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phonenumber'],
                api.payload['language'],
                api.payload['currency'])
        provider_id = mod.Provider().insert(args)
        api.payload['id'] = provider_id
        return api.payload


@provider_ns.route("/<int:id>")
class Provider(Resource):

    @api.marshal_with(ser.Provider().get)
    def get(self, id):
        """
        Displays the provider detail
        """
        return mod.Provider().one(args=(id,))

    @api.expect(ser.Provider().edit, validate=True)
    @api.marshal_with(ser.Provider().get)
    def put(self, id):
        """
        Edits the selected provider
        """
        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phonenumber'],
                api.payload['language'],
                api.payload['currency'],
                api.payload['id'])
        mod.Provider().update(args)
        return api.payload
