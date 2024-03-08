import datetime

date = datetime.timedelta(days = int(input('Enter a date:\n')))
today = datetime.datetime.now()
date1 = today - date
delta = today - date1        


print(delta.total_seconds)