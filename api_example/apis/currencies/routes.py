from flask_restplus import Resource
from flask import abort
from .namespaces import api
from . import models
from .marshallers import currency_marsh

currency_mod = models.Currency()


@api.route("/")
class CurrencyList(Resource):

    @api.marshal_list_with(currency_marsh)
    def get(self):
        """
        Returns the list of currencies
        """
        return [cur for cur in currency_mod.all()]


@api.route("/<string:code>")
class Currency(Resource):

    @api.marshal_with(currency_marsh)
    def get(self, code):
        """
        Displays the currency detail
        """
        code = code.upper()
        cur = currency_mod.one(code)
        if not cur:
            abort(404, f"No such currency: {code}")
        return cur
