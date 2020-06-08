import datetime
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
def addYears(time,y):
    try:        
        return time.replace(year = time.year + y)
    except ValueError:   
        return time + (date(time.year + y, 1, 1) - date(time.year, 1, 1))

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))

