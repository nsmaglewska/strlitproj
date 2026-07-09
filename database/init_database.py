import sqlite3

conn = sqlite3.connect("foods.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS foods(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    calories REAL,
    protein REAL,
    fat REAL,
    carbohydrates REAL,
    fiber REAL,
    sugar REAL
)
""")

conn.commit()
conn.close()

print("Baza została utworzona.")
