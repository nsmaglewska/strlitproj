import pandas as pd
import sqlite3

df = pd.read_csv(
    "products.csv",
    sep="\t",
    low_memory=False
)
df = df[
[
"name",
"energy-kcal_100g",
"proteins_100g",
"fat_100g",
"carbohydrates_100g",
"sugars_100g",
"fiber_100g"
]
]
df.columns = [
"name",
"calories",
"protein",
"fat",
"carbs",
"sugar",
"fiber"
]
conn = sqlite3.connect(
    "database/foods.db"
)
df.to_sql(
    "foods",
    conn,
    if_exists="replace",
    index=False
)
cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM foods"
)

print(
    cursor.fetchone()
)

cursor.execute(
    "SELECT * FROM foods LIMIT 3"
)

print(
    cursor.fetchall()
)
conn.close()
