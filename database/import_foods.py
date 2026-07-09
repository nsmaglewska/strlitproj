import sqlite3
import pandas as pd

df = pd.read_csv(
    "en.openfoodfacts.org.products.csv",
    sep="\t",
    low_memory=False
)

columns = [
    "product_name",
    "brands",
    "energy-kcal_100g",
    "proteins_100g",
    "fat_100g",
    "carbohydrates_100g",
    "sugars_100g",
    "fiber_100g",
    "salt_100g"
]

df = df[columns]

df.columns = [
    "product_name",
    "brands",
    "calories",
    "protein",
    "fat",
    "carbohydrates",
    "sugars",
    "fiber",
    "salt"
]

df = df.dropna(subset=["product_name"])

conn = sqlite3.connect("foods.db")

df.to_sql(
    "foods",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Import zakończony.")
