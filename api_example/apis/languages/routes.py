"""
Routes and views for the current endpoint
"""
from flask_restplus import Resource
from flask import abort
from .namespaces import api
from . import models
from .marshallers import language_marsh

language_mod = models.Language()


@api.route("/")
class LanguageList(Resource):

    @api.marshal_list_with(language_marsh)
    def get(self):
        """
        Returns the list of languages
        """
        return language_mod.all()


@api.route("/<string:code>")
class Language(Resource):

    @api.marshal_with(language_marsh)
    def get(self, code):
        """
        Displays the language detail
        """
        # language codes are always lower in pycountry
        code = code.lower()

        lang = language_mod.one(code)

        # abort if lang not found
        if not lang:
            abort(404, f"No such language: {code}")
        return lang
