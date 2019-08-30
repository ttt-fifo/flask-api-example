from flask import Flask
from .extensions.flask_sqlite3 import SQLite3
from .config import Config


app = Flask(__name__)
app.config.from_object(Config())
db = SQLite3(app)
