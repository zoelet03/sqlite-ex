#!/usr/bin/env python3


import sqlite3


DATABASE_FILE = 'tutors.db'


def connect(db_file=DATABASE_FILE):
    try:
        con = sqlite3.connect(db_file)
        return con
    except sqlite3.Error as e:
        print(e)


def disconnect(connection):
    connection.close()
