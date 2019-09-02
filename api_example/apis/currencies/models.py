import pycountry


class Currency:

    def all(self):
        for cur in pycountry.currencies:
            dat = {}
            dat['code'] = cur.alpha_3
            dat['name'] = cur.name
            yield dat

    def one(self, code):
        cur = pycountry.currencies.get(alpha_3=code)
        if cur:
            result = {'code': cur.alpha_3, 'name': cur.name}
        else:
            result = None
        return result
