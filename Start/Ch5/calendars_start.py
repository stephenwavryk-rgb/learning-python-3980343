#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
# c = calendar.TextCalendar(calendar.MONDAY)
# thestr = c.formatmonth(2026,1,0,0)
# print(thestr)

# from code challenge
# get an array of week lists
# [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]
weekslist = calendar.monthcalendar(2025, 12)
print(weekslist)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr = hc.formatmonth(2026,1)
# print(thestr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2026, 8):
#   print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#   print(name)

# for day in calendar.day_name:
#   print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
# print("Teams meetings will be on:")
# for m in range(1,13):
#   cal = calendar.monthcalendar(2026, m)
#   weekone = cal[0]
#   weektwo = cal[1]
#   if weekone[calendar.FRIDAY] != 0:
#     meetday = weekone[calendar.FRIDAY]
#   else:
#     meetday = weektwo[calendar.FRIDAY]

#   print(f"{calendar.month_name[m]}:  {meetday}")

# -------------

