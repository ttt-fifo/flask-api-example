from flask_restplus import Api
from . import providers
from . import languages

api = Api(title='Example API',
          version='0.1.0',
          description='Flask Restplus Example API')

api.add_namespace(providers.namespaces.api, path='/providers')
api.add_namespace(languages.namespaces.api, path='/languages')
