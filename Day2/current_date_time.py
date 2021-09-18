from datetime import datetime

# datetime object containing current date and time
Current_date_time = datetime.today()
 

date_Time = Current_date_time.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date Time :", date_Time)