from datetime import datetime
import time

# Different ways to create datetime objects
dt1 = datetime(2025, 12, 25)                  # specific date
dt2 = datetime.now()                          # right now (with microseconds)
dt = datetime.strptime("2025-12-25", "%Y-%m-%d")  # from string
dt = datetime.fromtimestamp(time.time())     # from timestamp

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)
