"""
@validate_with(...) decorator
"""
from functools import wraps
from flask import abort


class validate_with:
    """
    @validate_with(...) decorator
    To be used with flask restplus to decorate the view methods:

        ....

        @api.marshal_with(marshaler_some)
        @api.expext(some_marshaler)
        @validate_with(api, validation_callback)
        def post(self, id):
            ....

    Parameters:
        api: current api object
        validator: any callable object to validate the payload. The payload is
                   given as first argument

    Returns:
        None, but aborts connection on exception in validator

    Validator development:
        with signature def somevalidator(payload):
        should raise exception on invalid payload
    """
    # TODO: how to interface with api without giving api as argument?

    def __init__(self, api, validator):
        self.api = api
        self.validator = validator

    def __call__(self, func):
        @wraps(func)
        def wrapper(*arg, **kwarg):
            try:
                # validation with the given validator (should raise exception
                # on invalid payload)
                self.validator(self.api.payload)
                # the actual function is also enclosed in try-except
                result = func(*arg, **kwarg)
            except Exception as e:
                abort(400, str(e))
            return result
        return wrapper
