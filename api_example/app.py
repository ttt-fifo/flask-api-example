#!/bin/env python3
from flask import Flask
import sqlite3
from flask import g
from flask import jsonify
from flask import request

app = Flask(__name__)


class Connection(sqlite3.Connection):

    def all(self, query, args=()):
        cur = self.execute(query, args)
        while True:
            row = cur.fetchone()
            if not row:
                break
            yield row
        cur.close()

    def one(self, query, args=()):
        cur = self.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        if rv:
            return rv[0]
        return None


DATABASE = 'db.sqlite3'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, factory=Connection)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def help():
    return 'HELP'


@app.route('/providers', methods=['GET'])
def list():
    db = get_db()
    q = "select id, name, email, phonenumber, language, currency from provider"
    return jsonify([dict(p) for p in db.all(q)])


@app.route('/providers', methods=['POST'])
def create():
    q = """insert into provider(name, email, phonenumber, language, currency)
values(?, ?, ?, ?, ?)
"""
    arg = (request.json['name'], request.json['email'],
           request.json['phonenumber'], request.json['language'],
           request.json['currency'])
    db = get_db()
    db.execute(q, arg)
    db.commit()
    return "OK"


if __name__ == '__main__':
    app.run()
