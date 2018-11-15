from datetime import date
from datetime import datetime
from datetime import timedelta

today_date = date.today()
print(today_date)
print(today_date.day)
print(today_date.month)
print(today_date.year)
print("weekday", today_date.weekday())
print("ctime", today_date.ctime())
print("isocalendar", today_date.isocalendar())
#print("fromordinal", today_date.fromordinal())
#print("fromtimestamp:", today_date.fromtimestamp())
print("isoweekday:", today_date.isoweekday())
#print("fromisoformat:", today_date.fromisoformat())
print("isoformat:", today_date.isoformat())
print("replace:", today_date.replace())
print("timetuple:", today_date.timetuple())
print("strftime:", today_date.strftime("%d %b %y"))
print("toordinal:", today_date.toordinal())

today = datetime.now()
weekday = datetime.weekday(today)
time = datetime.time
print(time)
print(today)
print(weekday)

today = datetime.today()
time_delta = timedelta(days=365, weeks=2)
print(time_delta)
print("today's date is: ", today)
print("1 year and 2 weeks from now will be: ", today + time_delta)