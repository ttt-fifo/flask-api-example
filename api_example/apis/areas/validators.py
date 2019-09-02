from shapely.geometry import Polygon
from shapely.wkt import loads as geoloads
from flask_restplus.errors import ValidationError


class Area:

    def validate_geom(self, payload):
        try:
            polygon = geoloads(payload)
        except Exception as e:
            raise ValidationError(f"Invalid geometry '{payload}': {e}")

        if not isinstance(polygon, Polygon):
            raise ValidationError(f"Invalid geometry: {payload}")
        elif not polygon.is_valid:
            raise ValidationError(f"Invalid geometry: {payload}")

    def __call__(self, payload):
        self.validate_geom(payload['geom'])
