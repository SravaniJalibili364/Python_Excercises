#Prompt user to enter year, month values and print the calendar for the combination.
import calendar
y=int(input("enter year"))
m=int(input("enter month"))
print(calendar.month(y,m))
