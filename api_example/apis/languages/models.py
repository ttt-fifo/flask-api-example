import pycountry


class Language:

    def all(self):
        for lang in pycountry.languages:
            dat = {}
            code = getattr(lang, 'alpha_2', None)
            if not code:
                code = lang.alpha_3
            dat['code'] = code
            dat['name'] = lang.name
            yield dat

    def one(self, code):
        if len(code) == 2:
            lang = pycountry.languages.get(alpha_2=code)
            result = {'code': lang.alpha_2, 'name': lang.name}
        elif len(code) == 3:
            lang = pycountry.languages.get(alpha_3=code)
            result = {'code': lang.alpha_3, 'name': lang.name}
        else:
            result = None
        return result
