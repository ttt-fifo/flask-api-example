from app import db


def provider_list():
    q = """select id, name, email,
           phonenumber, language, currency from provider"""
    return [prov for prov in db.con.all(q)]
