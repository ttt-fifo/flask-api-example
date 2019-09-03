from flask_restplus import Resource
from core.lib.validators import validate_with
from .namespaces import api
from .marshallers import area_get_marsh
from .marshallers import area_edit_marsh
from . import validators
from . import models

area_mod = models.Area()
area_val = validators.Area()


@api.route("/")
class AreaList(Resource):

    @api.marshal_list_with(area_get_marsh)
    def get(self):
        """
        Returns the list of areas
        """
        return area_mod.all()

    @api.expect(area_edit_marsh, validate=True)
    @api.marshal_with(area_get_marsh)
    @validate_with(api, area_val)
    def post(self):
        """
        Adds a new area to the list
        """
        api.payload['provider'] = int(api.payload['provider'].split('/')[-1])
        args = (api.payload['name'],
                api.payload['price'],
                api.payload['geom'],
                api.payload['provider'])
        return area_mod.insert(args)


@api.route("/<int:id>")
class Area(Resource):

    @api.marshal_with(area_get_marsh)
    def get(self, id):
        """
        Displays the area details
        """
        return area_mod.one(args=(id,))

    @api.expect(area_edit_marsh, validate=True)
    @api.marshal_with(area_get_marsh)
    @validate_with(api, area_val)
    def put(self, id):
        """
        Edits the selected area
        """
        api.payload['provider'] = int(api.payload['provider'].split('/')[-1])
        args = (api.payload['name'],
                api.payload['price'],
                api.payload['geom'],
                api.payload['provider'],
                id)
        return area_mod.update(args)


@api.route("/<string:point>")
class AreaPoint(Resource):

    @api.marshal_list_with(area_get_marsh)
    def get(self, point):
        """
        Queries Areas Where Point Resides
        """
        return area_mod.query_point(arg=(point,))
