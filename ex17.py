#date and time

from datetime import datetime

now = datetime.now()


current_year = now.year
current_month = now.month
current_day = now.day

print now
print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s.%s.%s' % (current_year, current_month, current_day)

current_hour = now.hour
current_minute = now.minute
current_second = now.second

print '%s:%s:%s' % (current_hour, current_minute, current_second)

print '%s/%s/%s %s:%s:%s' % (current_month, current_day, current_year, current_hour, current_minute, current_second)
