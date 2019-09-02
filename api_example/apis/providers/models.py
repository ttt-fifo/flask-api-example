from core import db


class Provider:

    def all(self):
        q = """SELECT id, name, email,
               phone, language, currency FROM provider"""
        return db.con.all(q)

    def insert(self, arg=()):
        q = """
INSERT INTO provider(name, email, phone, language, currency)
VALUES (?, ?, ?, ?, ?)"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result

    def one(self, args=()):
        q = """SELECT id, name, email, phone, language, currency
FROM provider
WHERE id = ?"""
        return db.con.one(q, args)

    def update(self, arg=()):
        q = """
UPDATE provider SET name=?, email=?, phone=?, language=?, currency=?
WHERE id = ?"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result
