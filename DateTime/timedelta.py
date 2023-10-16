from datetime import datetime,timedelta

now = datetime.now()
print("Now : ",now.strftime("%d-%b-%Y"))

past_days = datetime.now() - timedelta(days=4)
print("Past : ",past_days.strftime("%d-%B-%y"))

past_weeks = datetime.now() - timedelta(weeks=4)
print("Past : ",past_weeks.strftime("%d-%B-%y"))


future = datetime(2050,5,15)
print("Future : ",future.strftime("%d-%b-%Y"))