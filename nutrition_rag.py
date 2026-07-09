from database.database import search_food

def retrieve_food_context(food_name):
    product = search_food(
        food_name
    )
    if product is None:
        return None
    context = f"""
Produkt:
{product['name']}
Wartości na 100g:
Kalorie:
{product['calories']} kcal
Białko:
{product['protein']} g
Tłuszcz:
{product['fat']} g
Węglowodany:
{product['carbs']} g
Cukry:
{product['sugar']} g
Błonnik:
{product['fiber']} g
"""
    return context
