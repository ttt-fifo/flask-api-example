from functools import wraps
from flask import abort

# TODO: how to connect with api without giving api as argument?


class validate_with:

    def __init__(self, api, validator):
        self.api = api
        self.validator = validator

    def __call__(self, func):
        @wraps(func)
        def wrapper(*arg, **kwarg):
            try:
                self.validator(self.api.payload)
                result = func(*arg, **kwarg)
            except Exception as e:
                abort(400, str(e))
            return result
        return wrapper
