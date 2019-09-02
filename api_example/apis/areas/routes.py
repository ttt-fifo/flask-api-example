from app import api
from flask_restplus import Resource
from . import models as mod
from . import serializers as ser

area_ns = api.namespace('areas', description='Areas Manipulation')


@area_ns.route("/")
class AreaList(Resource):

    @api.marshal_list_with(ser.Area().get)
    def get(self):
        """
        Returns the list of areas
        """
        return mod.Area().all()

    @api.expect(ser.Area().edit, validate=True)
    @api.marshal_with(ser.Area().get)
    def post(self):
        """
        Adds a new area to the list
        """
        args = (api.payload['name'],
                api.payload['price'],
                api.payload['geom'])
        area_id = mod.Area().insert(args)
        api.payload['id'] = area_id
        return api.payload
