import datetime
class Datetime():
    def time(self,string):
        self.date = datetime.datetime.strptime(string,'%b %d %Y %I:%M%p')
        return self.date
    

dttime= Datetime()
print(dttime.time('Jul 1 2014 2:43PM'))

