import datetime
today = "Feb 2 2019"
today_date = datetime.datetime.strptime(today,'%b %d %Y')
def  date(new_date):
    new_date = datetime.datetime.strptime(new_date,'%b %d %Y')
    difference = today_date-new_date
    if difference.days == 1:
        return "Yesterday"
    elif difference.days == -1:
        return "Tomorrow"
    elif difference.days == 0:
        return "Today"
    elif difference.days > 1:
        return f"{difference.days} days ago"
    elif difference.days < -1:
        return f"{difference.days} days after"
    

    
print(date('Feb 2 2019'))
print(date('Feb 1 2019'))
print(date('Jan 31 2019'))
print(date('Feb 3 2019'))

