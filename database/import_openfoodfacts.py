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
    "foods.db"
)
df.to_sql(
    "foods",
    conn,
    if_exists="replace",
    index=False
)
conn.close()
