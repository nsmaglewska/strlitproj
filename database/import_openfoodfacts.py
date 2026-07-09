import pandas as pd
import sqlite3
import os

DATABASE = "database/foods.db"
os.makedirs(
    "database",
    exist_ok=True
)
df = pd.read_csv(
    "database/products.csv",
    sep="\t",
    low_memory=False
)
columns = [
    "product_name",
    "energy-kcal_100g",
    "proteins_100g",
    "fat_100g",
    "carbohydrates_100g",
    "sugars_100g",
    "fiber_100g"
]
df = df[columns]
df.columns = [
    "name",
    "calories",
    "protein",
    "fat",
    "carbs",
    "sugar",
    "fiber"
]
df = df.dropna(
    subset=["name"]
)
conn = sqlite3.connect(
    DATABASE
)
df.to_sql(
    "foods",
    conn,
    if_exists="replace",
    index=True,
    index_label="id"
)
conn.close()


print(
    "Baza SQLite utworzona"
)
