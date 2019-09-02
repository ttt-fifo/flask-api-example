from core import db


class Area:

    def all(self):
        q = "SELECT id, name, price, AsText(geom) as geom FROM area"
        db.con.enable_spatialite()
        return db.con.all(q)

    def insert(self, arg=()):
        q = """
INSERT INTO area(name, price, geom)
VALUES(?, ?, GeomFromText(?, 4326))"""
        db.con.enable_spatialite()
        cur = db.con.cursor()
        cur.execute(q, arg)
        db.con.commit()
        result = cur.lastrowid
        cur.close()
        return result

    def one(self, args=()):
        q = "SELECT id, name, price, AsText(geom) as geom FROM area WHERE id=?"
        db.con.enable_spatialite()
        return db.con.one(q, args)

    def update(self, arg=()):
        q = """
UPDATE area
SET
    name=?,
    price=?,
    geom=GeomFromText(?, 4326)
WHERE id=?"""
        db.con.enable_spatialite()
        cur = db.con.cursor()
        cur.execute(q, arg)
        result = cur.lastrowid
        db.con.commit()
        cur.close()
        return result
