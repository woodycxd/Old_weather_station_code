"""
http://tempo-db.com/api/read-series/#read-series-by-key
"""

import datetime
from tempodb import Client

# Modify these with your settings found at: http://tempo-db.com/manage/
API_KEY = 'baff599bbda949d48a223633b75569e0'
API_SECRET = '79b79d2883874542a217afc9045b05e0'
SERIES_KEY = 'test1'

client = Client(API_KEY, API_SECRET)

start = datetime.date(2012, 1, 1)
end = start + datetime.timedelta(days=1)

data = client.read_key(SERIES_KEY, start, end)

for datapoint in data.data:
    print datapoint
