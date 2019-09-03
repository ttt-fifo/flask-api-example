"""
Models for the current endpoint
"""
import pycountry


class Currency:
    """
    Model without db queries.
    Gets data from pycountry
    """

    def all(self):
        """
        Returns full list of all currencies
        """
        data = []
        for cur in pycountry.currencies:
            dat = {}
            dat['code'] = cur.alpha_3
            dat['name'] = cur.name
            data.append(dat)
        return data

    def one(self, code):
        """
        Returns one currency by given currency code
        """
        cur = pycountry.currencies.get(alpha_3=code)
        if cur:
            result = {'code': cur.alpha_3, 'name': cur.name}
        else:
            result = None
        return result
