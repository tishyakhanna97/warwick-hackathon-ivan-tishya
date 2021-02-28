import csv



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

ing = ['blueberries', 'butter', 'eggs', 'lemon zest', 'milk', 'other things needed']


print(match_ingredients(ing))