"""
Validators for the current endpoint
"""
import pycountry
from flask_restplus.errors import ValidationError


class Provider:
    """
    Provider validator
    """

    def validator_language(self, payload):
        """
        Validator for the language field
        Checks if language can be found by given code
        (the payload is lang code)
        The code could be 2 alphabets or 3 alphabets
        """

        # only low caps codes in the pycountry.languages
        payload = payload.lower()

        # get the current language
        if len(payload) == 2:
            lang = pycountry.languages.get(alpha_2=payload)
        elif len(payload) == 3:
            lang = pycountry.languages.get(alpha_3=payload)
        else:
            lang = None

        # if lang does not exist, raise validation error
        # (the error will be catched by @validate_with(...) decorator
        if not lang:
            raise ValidationError(f"Invalid language: {payload}")

    def validator_currency(self, payload):
        """
        Currency field validator
        Checks if currency code (the payload) could be found in pycountry
        """

        # currency codes are always big caps in pycountry
        payload = payload.upper()

        # check for three alphabet code
        cur = pycountry.currencies.get(alpha_3=payload)

        # raise validation error if code not found
        if not cur:
            raise ValidationError(f"Invalid currency: {payload}")

    def __call__(self, payload):
        """
        When this validator is called as a function, it will perform
        the following logic
        """

        # validate the two fields
        self.validator_language(payload['language'])
        self.validator_currency(payload['currency'])
