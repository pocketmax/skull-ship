# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
import os
import pandas as pd
import numpy as np

cls = lambda: os.system('clear')
cls()

import datetime
dti = pd.to_datetime(
  ["1/1/2018", np.datetime64("2018-01-01"), datetime.datetime(2018, 1, 1)]
)

print('\ntime index...')
print(dti)

print('\ntime range...')
dti2 = pd.date_range("2018-01-01", periods=10, freq="H")
dti2 = dti2.tz_localize("UTC")
print(dti2)

print('\nconvert timezone...')
dti2.tz_convert("US/Pacific")

# dti2 = dti2.tz_localize("UTC")
# print(dti2)
#
# dti2 = dti2.tz_convert("US/Pacific")
# print(dti2)
#
# idx = pd.date_range("2018-01-01", periods=5, freq="H")
# ts = pd.Series(range(len(idx)), index=idx)
# print(ts)
# ts = ts.resample("2H").mean()
# print(ts)
#
# friday = pd.Timestamp("2018-01-05")
# print(friday.day_name())
#
# saturday = friday + pd.Timedelta("1 day")
# print(saturday.day_name())
#
# monday = friday + pd.offsets.BDay()
# print(monday.day_name())
