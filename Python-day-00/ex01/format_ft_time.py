# Using datetime function
# from datetime import datetime

# d = datetime.now()
# print(f"Seconds since January 1, 1970: {d.timestamp():,.4f} or \
# {d.timestamp():.2e} in scientific notation")
# print(d.strftime("%b %d %Y"))

# Using time function
import time

s = time.time()
print(f"Seconds since January 1, 1970: {s:,.4f} or {s:.2e} \
in scientific notation")
print(f"{time.strftime('%b %d %Y')}")
