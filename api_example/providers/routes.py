from flask import jsonify
from flask import request
from app import app
from app import db


@app.route('/providers', methods=['GET'])
def list_providers():
    q = "select id, name, email, phonenumber, language, currency from provider"
    return jsonify([p for p in db.con.all(q)])


@app.route('/providers', methods=['POST'])
def create_provider():
    q = """insert into provider(name, email, phonenumber, language, currency)
values(?, ?, ?, ?, ?)
"""
    arg = (request.json['name'], request.json['email'],
           request.json['phonenumber'], request.json['language'],
           request.json['currency'])
    db.con.execute(q, arg)
    db.con.commit()
    return "OK"
