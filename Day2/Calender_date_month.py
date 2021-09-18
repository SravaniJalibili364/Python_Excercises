'''# Python program to display calendar of
# given month of the year'''

import calendar

Year = int(input("Enter Year: "))
Month = int(input("Enter Month: "))

# To display the calendar
print(calendar.month(Year,Month))


