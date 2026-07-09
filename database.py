import sqlite3

DATABASE = "foods.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def search_food(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM foods
        WHERE LOWER(name) LIKE LOWER(?)
    """, (f"%{name}%",))

    result = cursor.fetchone()

    conn.close()

    return result
