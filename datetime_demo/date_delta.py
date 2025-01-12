#delta --> difference
from datetime import datetime, timedelta
from http.cookiejar import cut_port_re

custom_date = datetime(2025,1,1,13,12,11,111)

#delta - 1 day
time_with_delta = custom_date - timedelta(days=1, hours=2)
print(time_with_delta)