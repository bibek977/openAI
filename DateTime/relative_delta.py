from dateutil.relativedelta import relativedelta
from datetime import datetime

now = datetime.now()
print("now : ",now.strftime("%d-%b-%y"))

past_month = datetime.now() - relativedelta(months=4)
print("past_month : ",past_month.strftime("%d-%b-%y"))

past_days = datetime.now() - relativedelta(days=2)
print("past_days : ",past_days.strftime("%d-%b-%y"))

past_weeks = datetime.now() - relativedelta(weeks=12)
print("past_weeks : ",past_weeks.strftime("%d-%b-%y"))

past_year = datetime.now() - relativedelta(years=3)
print("past_year : ",past_year.strftime("%d-%B-%Y"))