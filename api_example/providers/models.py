from application import db


class Provider:

    def all(self):
        q = """select id, name, email,
               phone, language, currency from provider"""
        return [prov for prov in db.con.all(q)]

    def insert(self, arg=()):
        q = """
insert into provider(name, email, phone, language, currency)
values (?, ?, ?, ?, ?)"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result

    def one(self, args=()):
        q = """select id, name, email, phone, language, currency
from provider
where id = ?"""
        return db.con.one(q, args)

    def update(self, arg=()):
        q = """
update provider set name=?, email=?, phone=?, language=?, currency=?
where id = ?"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result
