#First in first out
from collections_temp import deque

operating_systems=deque(["Windows","Linux","Mac"])
print(operating_systems)
operating_systems.append("Chromium")
item=operating_systems.popleft()
print(item)



# var = operating_systems[1:1]
# print(var)