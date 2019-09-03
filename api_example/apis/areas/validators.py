"""
Validators for the current endpoint
"""
from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.wkt import loads as geoloads
from flask_restplus.errors import ValidationError


class Area:
    """
    Validates area entry
    """

    def validate_geom(self, payload):
        """
        Validates the geometry field
        """

        # load wkt
        try:
            polygon = geoloads(payload)
        except Exception as e:
            raise ValidationError(f"Invalid geometry '{payload}': {e}")

        # check polygon for validity
        if not isinstance(polygon, Polygon):
            raise ValidationError(f"Invalid geometry: {payload}")
        elif not polygon.is_valid:
            raise ValidationError(f"Invalid geometry: {payload}")

    def __call__(self, payload):
        """
        When invoked as a function this logic is executed
        """
        self.validate_geom(payload['geom'])


def point_validator(string):
    """
    Validates if wkt string is a point
    """
    try:
        point = geoloads(string)
    except Exception as e:
        raise ValidationError(f"Invalid point geometry '{string}': {e}")

    if not isinstance(point, Point):
        raise ValidationError(f"Invalid point geometry: '{string}'")
