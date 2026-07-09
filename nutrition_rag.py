from database.database import search_food

def retrieve_food_context(food_name):
    product = search_food(food_name)

    if product is None:
        return None

    context = f"""
Nazwa produktu: {product["product_name"]}

Producent: {product["brands"]}

Wartości odżywcze w 100 g:

Kalorie: {product["calories"]} kcal
Białko: {product["protein"]} g
Tłuszcz: {product["fat"]} g
Węglowodany: {product["carbohydrates"]} g
Cukry: {product["sugars"]} g
Błonnik: {product["fiber"]} g
Sól: {product["salt"]} g
"""

    return context
