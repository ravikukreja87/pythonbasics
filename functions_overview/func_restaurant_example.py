def make_dish(dish_name, dish_category, **options):
    print(f'Order received for {dish_name} under {dish_category} category')
    if options:
        print(f'\tOptions:-')
        for key, value in options.items():
            print(f'\t{key}-> {value}')


make_dish('pizza', 'italian', herbs='yes', toppings=3, crust='pan')  # dish_name, dish_category, few attributes
make_dish('pizza', 'italian', herbs='yes', toppings=2)
make_dish('pizza', 'italian', toppings=1)
make_dish('pizza', 'italian')
make_dish('bread', 'general', type='Wheat')
make_dish('bread', 'general', type='Wheat', qty=5)
