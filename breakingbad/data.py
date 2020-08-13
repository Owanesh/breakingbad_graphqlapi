import sqlite3
from sqlite3 import Error


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_connection():
    database = "database.sqlite"
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = dict_factory
        return conn
    except Error as e:
        print(e)


def select_all(table: str, jsonify=False) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table)
    rows = cur.fetchall()
    conn.close()
    print(rows[0])
    return rows


def select_by_column(table: str, column: str, value, jsonify=False) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table + " WHERE " + column + "=?", (value,))
    rows = cur.fetchall()
    conn.close()
    return rows
