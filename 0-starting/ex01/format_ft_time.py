from datetime import datetime

time_now = datetime.now()

tn_ts = time_now.timestamp()
print(f"Seconds since January 1, 1970: {tn_ts:,} or {tn_ts:.2e} "
      + "in scientific notation")

print(f"{time_now:%b %d %Y}")
