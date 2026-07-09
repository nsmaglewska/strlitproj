import sqlite3

DATABASE = "database/foods.db"
def search_food(name):
    conn = sqlite3.connect(
        DATABASE
    )
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM foods
        WHERE LOWER(name)
        LIKE LOWER(?)
        LIMIT 1
        """,
        (
            f"%{name}%",
        )
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None
