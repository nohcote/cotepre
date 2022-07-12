from datetime import datetime,timezone
now_utc = datetime.now(timezone.utc) # UTC+0
print(now_utc.strftime('%Y-%m-%d'))