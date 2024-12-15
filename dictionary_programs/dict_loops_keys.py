# Loop through keys of dictionary

categories_fruits_vegetables = {"Apple": "Fruit", "Mango": "Fruit", "Tomato": "Vegetable", "Potato": "Vegetable",
                                "Onion": "Vegetable"
                                }

# for fruit_or_veg, category in categories_fruits_vegetables.items():
#     print(f'{fruit_or_veg} is a {category}')

print("=========================")
special_value = 'Tomato'
for key in categories_fruits_vegetables.keys():
    print(f'{key} is a {categories_fruits_vegetables[key]}')
    if key == special_value:
        print(f'\tIt is considered as fruit also')
