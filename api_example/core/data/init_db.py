#!/bin/env python3
"""
Script to init db
"""
import os
import sqlite3

# cwd to the current script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# init db
con = sqlite3.connect('db.sqlite3')
con.enable_load_extension(True)
with open('init_db.sql', 'r') as f:
    con.executescript(f.read())
