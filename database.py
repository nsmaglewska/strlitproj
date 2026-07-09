import sqlite3

DB_PATH = "foods.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def search_food(name):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM foods
        WHERE name LIKE ?
    """, (f"%{name}%",))

    rows = cursor.fetchall()

    conn.close()

    return rows
