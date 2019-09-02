import re
import pycountry
from flask_restplus.errors import ValidationError

re_email = re.compile(r'\S+@\S+\.\S+')
re_phone = re.compile(r'\+.\d+')


class Provider:

    def __init__(self):
        self.field_validators = {'email': self.validator_email,
                                 'language': self.validator_language,
                                 'currency': self.validator_currency,
                                 'phone': self.validator_phone}

    def validator_email(self, payload):
        m = re_email.match(payload)
        if not m:
            raise ValidationError(f"Invalid email: {payload}")

    def validator_language(self, payload):
        if len(payload) == 2:
            lang = pycountry.languages.get(alpha_2=payload)
        elif len(payload) == 3:
            lang = pycountry.languages.get(alpha_3=payload)
        else:
            lang = None

        if not lang:
            raise ValidationError(f"Invalid language: {payload}")

    def validator_currency(self, payload):
        payload = str(payload).upper()
        cur = pycountry.currencies.get(alpha_3=payload)
        if not cur:
            cur = pycountry.currencies.get(numeric=payload)

        if not cur:
            raise ValidationError(f"Invalid currency: {payload}")

    def validator_phone(self, payload):
        m = re_phone.match(payload)
        if not m:
            raise ValidationError(f"Invalid phone number: {payload}")

    def __call__(self, payload):

        for field, validator in self.field_validators.items():
            data = payload.get(field, None)
            if data:
                validator(data)
