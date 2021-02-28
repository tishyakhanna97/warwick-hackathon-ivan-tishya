import csv
import requests


def combined(item):
    json_product = requests.get(generate_request_for_spoonacular(item))
    id = get_product_id(json_product)
    try:
        req = generate_request_for_product(id)
        json_ingredients = requests.get(req).json()['ingredients']
    except:
        print("Failed at the ingredients")
        return [["Nothing", "Try Something Else"]]
    final_ingredients = [obj["name"] for obj in json_ingredients]
    print(final_ingredients)
    return match_ingredients(final_ingredients)



def generate_request_for_spoonacular(item):
    item = item.replace(" ","+")
    x=  f"https://api.spoonacular.com/recipes/complexSearch?apiKey=f9c09a3f181a42f28aace38e8dc2914b&query={item}&number=1"
    x = x.rstrip("\n")
    x = x.rstrip()
    print(x)
    return x

def get_product_id(json_input):
    try:
        converted = json_input.json()
        id = converted['results'][0]["id"]
        return id
    except:
        print("Nothing Found")


def generate_request_for_product(id):
    return f"https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=f9c09a3f181a42f28aace38e8dc2914b"

def match_ingredients(ingredients):
    source_file = "data/data_for_flask.csv"
    final_set = []
    with open(source_file) as f:
        data = csv.reader(f)
        for row in data:
            data_item = row[0]
            for x in ingredients:
                if data_item in x:
                    temp = []
                    temp.append(x)
                    temp.append(row[5])
                    final_set.append(temp)
                    break
    return final_set
