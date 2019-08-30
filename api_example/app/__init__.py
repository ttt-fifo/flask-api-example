from flask import Flask
from .extensions.flask_sqlite3 import SQLite3
from .config import Config
from flask_restplus import Api


app = Flask(__name__)
app.config.from_object(Config())
api = Api(app=app)
db = SQLite3(app)
