import sqlite3
from flask import g
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = 'Registros_apostas.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db_path = os.path.join(BASE_DIR, DATABASE)
        db = g._database = sqlite3.connect(db_path)
        db.row_factory = dict_factory
    return db

class SQLite:

    def __init__(self):
        self.db = get_db()

    def make_dicts(self, cursor, row):
        return dict((cursor.description[idx][0], value)
            for idx, value in enumerate(row)) 

    def select(self, query, args=(), one=False):
        cur = self.db.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
