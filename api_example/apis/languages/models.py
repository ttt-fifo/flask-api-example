"""
Models for the current endpoint
"""
import pycountry


class Language:
    """
    Model without database query
    Gets languages from pycountry
    """

    def all(self):
        """
        Returns the list of languages
        """
        data = []
        for lang in pycountry.languages:
            dat = {}
            code = getattr(lang, 'alpha_2', None)
            if not code:
                code = lang.alpha_3
            dat['code'] = code
            dat['name'] = lang.name
            data.append(dat)
        return data

    def one(self, code):
        """
        Returns one language by given code
        """
        result = None
        if len(code) == 2:
            lang = pycountry.languages.get(alpha_2=code)
            if lang:
                result = {'code': lang.alpha_2, 'name': lang.name}
        elif len(code) == 3:
            lang = pycountry.languages.get(alpha_3=code)
            if lang:
                result = {'code': lang.alpha_3, 'name': lang.name}
        return result
