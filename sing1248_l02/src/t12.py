"""
-------------------------------------------------------
[Lab 2, Task 12]
-------------------------------------------------------
Author:  Sukhman Singh
ID:      169061248
Email:   sing1248@mylaurier.ca
__updated__ = "2023-09-14"
-------------------------------------------------------
"""
HOURS_PER_DAY = 24
SECONDS_PER_MINUTE = 60

seconds = int(input("Number of seconds: "))

days = int(seconds/86400)
days_seconds = seconds - (days*86400)

hours = int(days_seconds/3600)
hours_seconds = days_seconds - (hours*3600)

minutes = int(hours_seconds/SECONDS_PER_MINUTE)
minutes_seconds = hours_seconds - (minutes*SECONDS_PER_MINUTE)

seconds = minutes_seconds

print("Days: ", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
