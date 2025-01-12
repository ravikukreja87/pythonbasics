from io import StringIO

import pandas

event_data = StringIO("""Date;Event;Number
01/11/2025;Cricket;1000
02/11/2025;Football;1100
01/10/2025;Hockey;500""")
#
# event_series = pandas.DataFrame(event_data)


event_series_formatted = pandas.read_csv(event_data, sep=";")
print(event_series_formatted)