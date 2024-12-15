audi = {'name': 'Audi', 'color': 'white', 'top_speed': 100, 'engine_capacity': 1500, 'year': 2009}
bmw = {'name': 'BMW', 'color': 'black', 'top_speed': 110, 'engine_capacity': 1800, 'year': 2006}
porsche = {'name': 'Porsche', 'color': 'cyan', 'top_speed': 160, 'engine_capacity': 2800, 'year': 2016}

# Above are 3 dictionaries

# One list of all these 3 dictionaries
car = [audi, bmw, porsche]  # Complex data structure --> List of Dictionaries
# print(car)

# for each_car in car:
# print("-------------")
# print(each_car['name'])
# print("Car Details -- ")
# for each_car_attributes in each_car.keys():
#     if each_car_attributes != 'name':
# print(each_car[each_car_attributes])

# print(car)
##########################################################################################
# print("########################################################")
# Complex data structure --> Dictionary of Lists as Values

fiction_books = ['fiction_book1', 'fiction_book2', 'fiction_book3']
horror_books = ['horror_book1', 'horror_book2', 'horror_book3']
self_help_books = ['sh_book1', 'sh_book2']

all_books = {
    'fiction': fiction_books,
    'horror': horror_books,
    "self_help": self_help_books
}
# print(all_books)

for book_category, list_of_books in all_books.items():
    print('----------')
    print(f'Book Category - {book_category}')
    print(list_of_books)
    if book_category == 'fiction':
        list_of_books.append("fiction_book4")
    for each_book in list_of_books:
        print(each_book)
