from core import db


class Area:

    def all(self):
        q = """
SELECT
    a.id AS id,
    a.name AS name,
    a.price AS price,
    AsText(a.geom) AS geom,
    p.id as provider_id,
    p.name as provider_name
FROM
    area AS a,
    provider AS p
WHERE a.provider = p.id
"""
        db.con.enable_spatialite()
        data = []
        for dat in db.con.all(q):
            dat['provider'] = {'id': int(dat['provider_id']),
                               'name': str(dat['provider_name'])}

            del dat['provider_id']
            del dat['provider_name']
            data.append(dat)
        return data

    def one(self, args=()):
        q = """
SELECT
    a.id AS id,
    a.name AS name,
    a.price AS price,
    AsText(a.geom) AS geom,
    p.id as provider_id,
    p.name as provider_name
FROM
    area AS a,
    provider AS p
WHERE a.provider = p.id
AND a.id = ?
"""
        db.con.enable_spatialite()
        data = db.con.one(q, args)
        data['provider'] = {'id': int(data['provider_id']),
                            'name': str(data['provider_name'])}
        del data['provider_id']
        del data['provider_name']
        return data

    def insert(self, arg=()):
        q = """
INSERT INTO area(name, price, geom, provider)
VALUES(?, ?, GeomFromText(?, 4326), ?)"""
        db.con.enable_spatialite()
        cur = db.con.cursor()
        cur.execute(q, arg)
        db.con.commit()
        id = cur.lastrowid
        cur.close()
        result = self.one(args=(id,))
        return result

    def update(self, arg=()):
        q = """
UPDATE area
SET
    name=?,
    price=?,
    geom=GeomFromText(?, 4326),
    provider=?
WHERE id=?"""
        db.con.enable_spatialite()
        cur = db.con.cursor()
        cur.execute(q, arg)
        db.con.commit()
        cur.close()
        id = arg[-1]
        result = self.one(args=(id,))
        return result

    def query_point(self, arg=()):
        q = """
SELECT
    a.id AS id,
    a.name AS name,
    a.price AS price,
    AsText(a.geom) AS geom,
    p.id as provider_id,
    p.name as provider_name
FROM
    area AS a,
    provider AS p
WHERE a.provider = p.id
AND Within(GeomFromText(?, 4326), geom)
"""
        db.con.enable_spatialite()
        data = []
        for dat in db.con.all(q, arg):
            dat['provider'] = {'id': int(dat['provider_id']),
                               'name': str(dat['provider_name'])}

            del dat['provider_id']
            del dat['provider_name']
            data.append(dat)
        return data
