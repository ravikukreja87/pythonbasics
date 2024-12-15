grocery_to_buy=['ballpen','bondpaper','ink','inkpen','fountainpen','pen','plainpaper']
grocery_purchased=[]
pens=[]
papers=[]
others=[]


while grocery_to_buy:
    eachItem = grocery_to_buy.pop()
    if 'pen' in eachItem:
        pens.append(eachItem)
    elif 'paper' in eachItem:
        papers.append(eachItem)
    else:
        others.append(eachItem)

print(f"Pens {pens}")
print(f"Others {others}")
print(f"Papers {papers}")

#move items from one list to another

# while grocery_to_buy:
#     item = grocery_to_buy.pop()
#     grocery_purchased.append(item)
#
# print(f"Grocery Purchased {grocery_purchased}")
# print(f"Grocery To Buy {grocery_to_buy}")