"""
Models for the current endpoint
"""
from core import db


class Area:
    """
    Area data model
    """

    def all(self):
        """
        Returns the list of all areas
        (provider data nested)
        """
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
        # enable spatial extension on the driver
        db.con.enable_spatialite()

        data = []
        for dat in db.con.all(q):

            # transform the provider fields
            dat['provider'] = {'id': int(dat['provider_id']),
                               'name': str(dat['provider_name'])}
            del dat['provider_id']
            del dat['provider_name']

            data.append(dat)
        return data

    def one(self, id):
        """
        Gets one area by id
        """
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
        # enable spatial extensions
        db.con.enable_spatialite()

        arg = (id,)
        data = db.con.one(q, arg)

        # transform the provider data
        data['provider'] = {'id': int(data['provider_id']),
                            'name': str(data['provider_name'])}
        del data['provider_id']
        del data['provider_name']

        return data

    def insert(self, arg=()):
        """
        Inserts one provider to the list
        """

        q = """
INSERT INTO area(name, price, geom, provider)
VALUES(?, ?, GeomFromText(?, 4326), ?)"""

        # enable spatial extension
        db.con.enable_spatialite()

        # insert
        cur = db.con.cursor()
        cur.execute(q, arg)
        db.con.commit()
        # this is geting the inserted row id
        id = cur.lastrowid
        cur.close()

        # get the area data back from the db by id
        result = self.one(id)
        return result

    def update(self, arg=()):
        """
        Updates one area by given id
        """

        q = """
UPDATE area
SET
    name=?,
    price=?,
    geom=GeomFromText(?, 4326),
    provider=?
WHERE id=?"""

        # enable spatialite
        db.con.enable_spatialite()

        # update the area
        cur = db.con.cursor()
        cur.execute(q, arg)
        db.con.commit()
        cur.close()

        # get back the data from db and return it
        id = arg[-1]
        result = self.one(id)
        return result

    def query_point(self, point):
        """
        Queries a given point
        Returns list of areas containing the point
        """

        # the query with spatial condition
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

        # query, transform, return the data
        db.con.enable_spatialite()
        data = []
        arg = (point,)
        for dat in db.con.all(q, arg):
            dat['provider'] = {'id': int(dat['provider_id']),
                               'name': str(dat['provider_name'])}

            del dat['provider_id']
            del dat['provider_name']
            data.append(dat)
        return data
