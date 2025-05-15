from datetime import datetime

now = datetime.now()

str_time = now.strftime("%Y-%m-%d")
print(str_time)