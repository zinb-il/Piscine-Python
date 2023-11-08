from datetime import datetime 
d = datetime.now()
print(f"Seconds since January 1, 1970: {d.timestamp():,.4f} or {d.timestamp():.2e} in scientific notation")
print(d.strftime("%b %d %Y"))
