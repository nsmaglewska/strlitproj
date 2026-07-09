import sqlite3

DATABASE = "database/foods.db"

def search_food(food_name):

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM foods
        WHERE LOWER(product_name) LIKE LOWER(?)
        LIMIT 1
    """, (f"%{food_name}%",))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return dict(row)
