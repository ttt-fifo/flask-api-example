from .namespaces import api
from flask_restplus import fields

language_fields = dict(
    code=fields.String(min_length=2, max_length=3,
                       description="Language Code"),
    name=fields.String(description="Language Name"))

language_marsh = api.model("Language", language_fields)
