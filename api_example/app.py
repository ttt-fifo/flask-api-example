#!/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlite3 import SQLite3

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLite3(app)


@app.route('/')
def help():
    return 'HELP'


@app.route('/providers', methods=['GET'])
def list():
    q = "select id, name, email, phonenumber, language, currency from provider"
    return jsonify([dict(p) for p in db.con.all(q)])


@app.route('/providers', methods=['POST'])
def create():
    q = """insert into provider(name, email, phonenumber, language, currency)
values(?, ?, ?, ?, ?)
"""
    arg = (request.json['name'], request.json['email'],
           request.json['phonenumber'], request.json['language'],
           request.json['currency'])
    db.con.execute(q, arg)
    db.con.commit()
    return "OK"


if __name__ == '__main__':
    app.run()
