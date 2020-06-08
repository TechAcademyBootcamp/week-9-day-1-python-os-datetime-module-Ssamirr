import datetime
class Date():
    def __str__(self):
        return f"""
Current date and time:{datetime.datetime.today()}
Current year:{datetime.datetime.today().strftime('%Y')}
Month of year:{datetime.datetime.today().strftime('%m')}
Week number of the year:{datetime.datetime.today().strftime('%W')}
Weekday of the week:{datetime.datetime.today().strftime('%w')}
Day of year:{datetime.datetime.today().strftime('%-j')}
Day of the month:{datetime.datetime.today().strftime('%-d')}
Day of week:{datetime.datetime.today().strftime('%a')}
                """
date = Date()
print(date)


