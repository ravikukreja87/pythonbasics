# Loop through keys of dictionary

categories_fruits_vegetables = {"Apple": "Fruit", "Mango": "Fruit", "Tomato": "Vegetable", "Potato": "Vegetable",
                                "Onion": "Vegetable", "Avocado": "Fruit", "Brocolli": "Vegetable"
                                }
exotics = ['Avocado','Brocolli']

for key in categories_fruits_vegetables.keys():
    print(f'{key} is a {categories_fruits_vegetables[key]}')
    if key in exotics:
        print(f'\t{key} is an exotic {categories_fruits_vegetables[key]}')
