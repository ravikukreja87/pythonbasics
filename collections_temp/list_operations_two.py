grocery_to_buy = ['fountainpen','ballpen', 'bondpaper', 'ink', 'inkpen', 'plainpaper','pen']
temp = grocery_to_buy.copy()

index = 0
while index < len(grocery_to_buy):
    index = 0
    item = temp[index]
    item.strip()
    if 'pen' in item.lower():
        print(f"Found item containing 'pen': {item}")
        temp.remove(item)
    index += 1


print(f"Grocery List after removing pen {grocery_to_buy}")