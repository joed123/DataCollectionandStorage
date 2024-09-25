import requests

import json
from dataprocess import process_data

api_key = 'V10HP4EQ10FO0YSJ'
symbol = 'AAPL'
base_url = 'https://www.alphavantage.co/query?'
query = f'function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'

# Fetch data from API (split the URL into multiple lines)
url = base_url + query
response = requests.get(url)
data = response.json()
print(data)

time_series = data['Time Series (Daily)']

# Store the data in a file (optional, for persistence)

with open('time_series.json', 'w') as f:
    json.dump(time_series, f)

# Process the API data
process_data(time_series)
