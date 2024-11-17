num=7
print(f"Table of {num}")

i=0
while i <= 10:
	print(f"{num} X {i} = {num * i}")
	i+=3 #i=i+3
	# i is loop count variable
	# Value of loop count variable must change in program (inside loop code/body) otherwise we fall into infinite loop
	# 11 <= 10 --> False


	# for i in range(1, 15):
	# 	print(f"{num} X {i} = {num * i}")
print("End of Program")