import requests

def get_food_data(product_name):

    url = "https://api.nal.usda.gov/fdc/v1/foods/search"

    params = {
        "api_key": API_KEY,
        "query": product_name,
        "pageSize": 1
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["foods"]:
        return None

    food = data["foods"][0]

    nutrients = {}

    for nutrient in food["foodNutrients"]:
        name = nutrient.get("nutrientName")
        value = nutrient.get("value")

        nutrients[name] = value

    return {
        "name": food["description"],
        "nutrients": nutrients
    }
