import pycountry
from flask_restplus.errors import ValidationError


class Provider:

    def validator_language(self, payload):
        payload = payload.lower()
        if len(payload) == 2:
            lang = pycountry.languages.get(alpha_2=payload)
        elif len(payload) == 3:
            lang = pycountry.languages.get(alpha_3=payload)
        else:
            lang = None

        if not lang:
            raise ValidationError(f"Invalid language: {payload}")

    def validator_currency(self, payload):
        payload = payload.upper()
        cur = pycountry.currencies.get(alpha_3=payload)
        if not cur:
            cur = pycountry.currencies.get(numeric=payload)

        if not cur:
            raise ValidationError(f"Invalid currency: {payload}")

    def __call__(self, payload):
        self.validator_language(payload['language'])
        self.validator_currency(payload['currency'])
