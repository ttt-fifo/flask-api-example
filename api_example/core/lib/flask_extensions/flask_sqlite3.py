import sqlite3
from flask import current_app, _app_ctx_stack


class ExtendedConnection(sqlite3.Connection):

    def all(self, query, args=()):
        cur = self.execute(query, args)
        while True:
            row = cur.fetchone()
            if not row:
                break
            yield row
        cur.close()

    def one(self, query, args=()):
        cur = self.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        if rv:
            return rv[0]
        return None

    def enable_spatialite(self):
        self.enable_load_extension(True)
        self.execute('SELECT load_extension("mod_spatialite.so")')
        # self.execute('SELECT InitSpatialMetaData(1);')


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


class SQLite3(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        con = sqlite3.connect(current_app.config['SQLITE3_DATABASE'],
                              factory=ExtendedConnection)
        con.row_factory = make_dicts
        return con

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()

    @property
    def con(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
            return ctx.sqlite3_db
