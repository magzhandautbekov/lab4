from datetime import datetime,timedelta

current_date_time = datetime.now()

subtracted = datetime.now() - timedelta(days=5)

print(current_date_time)
print(subtracted)


