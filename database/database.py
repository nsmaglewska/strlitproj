import sqlite3
import os
DATABASE = "database/foods.db"
def search_food(name):
    name = name.lower().strip()
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM foods
        WHERE LOWER(name) LIKE ?
        LIMIT 1
        """,
        (
            f"%{name}%",
        )
    )
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None
