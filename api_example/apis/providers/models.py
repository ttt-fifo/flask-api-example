"""
Models for current endpoint
"""
from core import db


class Provider:
    """
    Provider data model
    """

    def all(self):
        """
        Returns the list of providers
        """
        q = """SELECT id, name, email,
               phone, language, currency FROM provider"""
        return [prov for prov in db.con.all(q)]

    def insert(self, arg=()):
        """
        Inserts one provider to the list
        arg: given from the view
        """
        q = """
INSERT INTO provider(name, email, phone, language, currency)
VALUES (?, ?, ?, ?, ?)"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result

    def one(self, id):
        """
        Returns one provider by given id
        """
        q = """SELECT id, name, email, phone, language, currency
FROM provider
WHERE id = ?"""
        args = (id,)
        return db.con.one(q, args)

    def update(self, arg=()):
        """
        Updates fields of the given provider
        """
        q = """
UPDATE provider SET name=?, email=?, phone=?, language=?, currency=?
WHERE id = ?"""
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result
