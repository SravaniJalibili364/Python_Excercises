from datetime import datetime

# datetime object containing current date and time
today= datetime.today()
 
print(today)

# dd/mm/YY 
date_time_= today.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", date_time_)