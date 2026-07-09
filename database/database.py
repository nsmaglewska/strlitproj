import sqlite3
import os
DATABASE = "database/foods.db"
def search_food(food_name):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM foods
        WHERE LOWER(name) LIKE LOWER(?)
        LIMIT 1
        """,
        (f"%{food_name}%",)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None
