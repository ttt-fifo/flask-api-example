#!/bin/env python3
from flask import Flask
from core import config
from core import db
from apis import api

app = Flask(__name__)
app.config.from_object(config.Config())
db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
