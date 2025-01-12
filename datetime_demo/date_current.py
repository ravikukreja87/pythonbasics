from datetime import datetime, timedelta

time_now = datetime.now()
print(time_now)

time_now_minus_two = time_now - timedelta(hours=2)
print(time_now_minus_two)

#See how many seconds are there in 100 mins
time_in_minutes = timedelta(minutes=100)
time_in_seconds = time_in_minutes.total_seconds()
print(time_in_seconds)