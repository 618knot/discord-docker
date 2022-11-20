import os
from dotenv import load_dotenv
import datetime
from ggcal import calendar_info3

# sche = calendar_info1()
now = datetime.datetime.now()
# # print(60 - now.second)
# print(sche[0])

# day_time = str(sche[0]).split("T")
# day = str(day_time[0]).split("-")
# time = str(day_time[1]).split(":")
# print(day)
# print(time)

print(datetime.datetime(year=2022, month=8, day=26).day-now.day == 0)
# print(datetime.timedelta(days=1) <=  now - datetime.datetime(year=2022, month=8, day=24, hour=23, minute=0) <= datetime.timedelta(days=1, seconds=59) )
# print(datetime.timedelta(days=1, seconds=59))
# print(now + datetime.timedelta(hours=9))]
print(now.day)