"""
http://tempo-db.com/api/write-series/#write-series-by-key
"""

import datetime
import random
from tempodb import Client, DataPoint

# Modify these with your credentials found at: http://tempo-db.com/manage/
API_KEY = 'baff599bbda949d48a223633b75569e0'
API_SECRET = '79b79d2883874542a217afc9045b05e0'
SERIES_KEY = 'test1'

client = Client(API_KEY, API_SECRET)

date = datetime.datetime(2012, 1, 1)

for day in range(1, 10):
    # print out the current day we are sending data for
    print date

    data = []
    # 1440 minutes in one day
    for min in range (1, 1441):
        data.append(DataPoint(date, random.random() * 50.0))
        date = date + datetime.timedelta(minutes=1)

    client.write_key(SERIES_KEY, data)
