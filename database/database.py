#import sqlite3
#import os
#DATABASE = "database/foods.db"
#def search_food(name):
#    name = name.lower().strip()
#    conn = sqlite3.connect(DATABASE)
#    conn.row_factory = sqlite3.Row
#    cursor = conn.cursor()
#    cursor.execute(
#        """
#        SELECT *
#        FROM foods
#        WHERE LOWER(name) LIKE ?
#        LIMIT 1
#        """,
#        (
#            f"%{name}%",
#        )
#    )
#    row = cursor.fetchone()
#    conn.close()
#    return dict(row) if row else None
import sqlite3
import os

DATABASE = "database/foods.db"


def search_food(name):

    print("DATABASE:", os.path.abspath(DATABASE))

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # sprawdzenie tabel
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    print("TABLES:", cursor.fetchall())


    # sprawdzenie struktury foods
    cursor.execute(
        "PRAGMA table_info(foods);"
    )

    print("COLUMNS:", cursor.fetchall())


    # test pobrania danych
    cursor.execute(
        "SELECT * FROM foods LIMIT 1"
    )

    test = cursor.fetchone()

    print("FIRST ROW:", test)


    conn.close()

    return dict(test) if test else None
