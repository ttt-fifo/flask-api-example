from .namespaces import api
from flask_restplus import fields

currency_fields = dict(
    code=fields.String(min_length=3, max_length=3,
                       description="Currency Code"),
    name=fields.String(description="Currency Name"))

currency_marsh = api.model("Currency", currency_fields)
