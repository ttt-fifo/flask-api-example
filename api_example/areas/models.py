from app import db


class Area:

    def all(self):
        q = "select id, name, price, geom from area"
        return [ar for ar in db.con.all(q)]

    def insert(self, arg=()):
        q = "insert into area(name, price, geom) values(?, ?, ?)"
        db.con.enable_spatialite()
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result

    def one(self, args=()):
        q = "select id, name, price, geom from area"
        return db.con.one(q, args)

    def update(self, arg=()):
        q = "update area set name=?, price=?, geom=? where id=?"
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result
