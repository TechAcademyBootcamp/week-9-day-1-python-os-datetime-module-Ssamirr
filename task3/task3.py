import datetime
class Time():
    def __str__(self):
        return f"Time:{datetime.datetime.now().time()}"

time = Time()
print(time)