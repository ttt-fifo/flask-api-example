from app import api
# from app import db
from flask_restplus import Resource

area_ns = api.namespace('areas', description='Areas Manipulation')


@area_ns.route("/")
class AreaList(Resource):

    def get(self):
        """
        Returns the list of areas
        """

    def post(self):
        """
        Adds a new area to the list
        """
