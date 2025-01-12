# Control flow provide an ability to achieve complex tasks
from datetime import datetime

# if statement

# 1. Read number from user
# 2. Check if number is greater than 10
# 3. Print on console if number is greater or smaller than 10


start_time = datetime.now()
num = int(input("Enter number : "))
if num > 10:
    print("Entered number is greater than 10")
elif num == 10:
    print("Entered number is equal to 10")
else:
    print("Entered number is less than 10")

end_time = datetime.now()
total_time = end_time - start_time #total_time is a duration or timedelta class
seconds_total_time = total_time.total_seconds()
print(f'Total time in seconds = {seconds_total_time} seconds')