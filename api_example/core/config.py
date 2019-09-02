import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLITE3_DATABASE = f'{BASE_DIR}/data/db.sqlite3'
