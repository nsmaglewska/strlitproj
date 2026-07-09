import pandas as pd
import sqlite3
import os

INPUT = "en.openfoodfacts.org.products.csv"
OUTPUT = "foods.db"
df = pd.read_csv(
    INPUT,
    sep="\t",
    low_memory=False,
    on_bad_lines="skip"
)
print("Dostępne kolumny:")
print(df.columns.tolist())
possible_columns = {
    "name": [
        "product_name",
        "product_name_en",
        "product_name_pl"
    ],
    "calories": [
        "energy-kcal_100g"
    ],
    "protein": [
        "proteins_100g"
    ],
    "fat": [
        "fat_100g"
    ],
    "carbs": [
        "carbohydrates_100g"
    ],
    "sugar": [
        "sugars_100g"
    ],
    "fiber": [
        "fiber_100g"
    ]
}
selected = {}
for new_name, options in possible_columns.items():

    for col in options:

        if col in df.columns:
            selected[new_name] = col
            break
print("Wybrane kolumny:")
print(selected)
df = df[
    list(selected.values())
]
df.columns = list(selected.keys())
df = df.dropna(
    subset=["name"]
)
df = df[
    df["name"].str.strip() != ""
]
df = df.drop_duplicates(
    subset=["name"]
)
df = df.head(10000)
conn = sqlite3.connect(
    OUTPUT
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
    "Utworzono foods.db:",
    len(df),
    "produktów"
)
