from datetime import datetime

custom_date = datetime(2024,12,25,11,22,12,111)
print(custom_date)

#DD-MM-YYYY
format_custom_date = custom_date.strftime('%d-%m-%Y')
print(format_custom_date)

format_with_time=custom_date.strftime('%d_%m_%Y %H:%M:%S')
print(format_with_time)

format_with_time=custom_date.strftime('%m_%d_%Y %H:%M:%S')
print(format_with_time)

format_with_time=custom_date.strftime('%B_%d_%Y %H:%M:%S')
print(format_with_time)
