from flask_restplus import Resource
from app import api
from . import models

provider_ns = api.namespace('providers', description='Providers Manipulation')


@provider_ns.route("/")
class ProviderList(Resource):

    def get(self):
        """
        Returns the list of providers
        """
        return models.provider_list()

    def post(self):
        """
        Adds a new provider to the list
        """


@provider_ns.route("/<int:id>")
class Provider(Resource):

    def get(self, id):
        """
        Displays the provider detail
        """

    def put(self, id):
        """
        Edits the selected provider
        """
