colors = ['GreeN','Red','Blue']
print(colors)

for eachColor in colors:
    if eachColor.lower() == 'blue':
        print("Blue is in list")
        break
    else:
        continue