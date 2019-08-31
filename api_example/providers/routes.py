from flask_restplus import Resource
from flask import abort
from app import api
from . import models
from . import serializers

provider_ns = api.namespace('providers', description='Providers Manipulation')
provider_serializer = serializers.Provider()
provider_model = models.Provider()


@provider_ns.route("/")
class ProviderList(Resource):

    @api.marshal_list_with(provider_serializer.get)
    def get(self):
        """
        Returns the list of providers
        """
        return provider_model.all()

    @api.expect(provider_serializer.edit, validate=True)
    @api.marshal_with(provider_serializer.get)
    def post(self):
        """
        Adds a new provider to the list
        """
        try:
            provider_serializer.validate_edit(api.payload)
        except Exception as e:
            abort(400, str(e))

        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phone'],
                api.payload['language'],
                api.payload['currency'])
        provider_id = provider_model.insert(args)
        api.payload['id'] = provider_id
        return api.payload


@provider_ns.route("/<int:id>")
class Provider(Resource):

    @api.marshal_with(provider_serializer.get)
    def get(self, id):
        """
        Displays the provider detail
        """
        return provider_model.one(args=(id,))

    @api.expect(provider_serializer.edit, validate=True)
    @api.marshal_with(provider_serializer.get)
    def put(self, id):
        """
        Edits the selected provider
        """
        try:
            provider_serializer.validate_edit(api.payload)
        except Exception as e:
            abort(400, str(e))

        args = (api.payload['name'],
                api.payload['email'],
                api.payload['phone'],
                api.payload['language'],
                api.payload['currency'],
                api.payload['id'])
        provider_model.update(args)
        return api.payload
