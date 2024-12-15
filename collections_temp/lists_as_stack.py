#Last in first out for elements i.e. its a Stack

grocery_to_buy=['ballpen','bondpaper','ink','inkpen','fountainpen','pen','plainpaper']
item=grocery_to_buy.pop()
print(item)
grocery_to_buy.append("eraser")
print(grocery_to_buy)
item=grocery_to_buy.pop()
print(item)
print(grocery_to_buy)
item=grocery_to_buy.pop()
print(item)