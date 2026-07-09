import requests

def get_food_data(product_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if len(data["products"]) == 0:
        return None

    return data["products"][0]
