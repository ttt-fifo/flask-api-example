"""
sqlite3 flask extension, taken from the flask documentation
and improved
"""
import sqlite3
from flask import current_app, _app_ctx_stack


def make_dicts(cursor, row):
    """
    Helper to make dicts from sqlite3 rows
    """
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


class ExtendedConnection(sqlite3.Connection):
    """
    Subclassing original sqlite3.Connection and adding

    # methods for easy quering, the idea taken from
    # https://postgres-py.readthedocs.io/en/latest/
    # https://github.com/3kwa/sql
    # https://github.com/kennethreitz/records
        con.one(..)
        con.all(..)

    # spatialite initialization
        con.enable_spatialite()
    """

    def all(self, query, args=()):
        """
        Method accepts sql query and returns all rows
        Implemented as a generator
        """
        cur = self.execute(query, args)
        while True:
            row = cur.fetchone()
            if not row:
                break
            yield row
        cur.close()

    def one(self, query, args=()):
        """
        Method takes sql and returns one row
        """
        cur = self.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        if rv:
            return rv[0]
        return None

    def enable_spatialite(self):
        """
        Enables spatialite extension on the current connection
        """
        self.enable_load_extension(True)
        self.execute('SELECT load_extension("mod_spatialite.so")')
        # self.execute('SELECT InitSpatialMetaData(1);')


class SQLite3(object):
    """
    sqlite3 flask plugin as described in flask documentation and improved
    """
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        # using extended connection class as described above
        con = sqlite3.connect(current_app.config['SQLITE3_DATABASE'],
                              factory=ExtendedConnection)
        # data returned to dicts
        con.row_factory = make_dicts
        return con

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def con(self):
        """
        This is the connection (for short con) to be used in the code
        like this:
        db.con.execute(...), db.con.execscript(..), etc.
        """
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db
