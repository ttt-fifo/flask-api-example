from flask import jsonify
# from flask import request
from app import app
from app import db


@app.route('/areas', methods=['GET'])
def list_areas():
    q = "select name, price, geom from area"
    return jsonify([p for p in db.con.all(q)])
