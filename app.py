import requests
import json
import pandas as pd
import pandas_ta as ta


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


def process_data(time_series):
    # Convert to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')

    # Convert columns from strings to appropriate numeric types
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype({
        'open': 'float',
        'high': 'float',
        'low': 'float',
        'close': 'float',
        'volume': 'int'
    })

    # Print or process the cleaned data
    print("Cleaned DataFrame:")
    print(df)

    # You can return the DataFrame if needed for further usage
    return df


def add_technical_indicators(df):
    # Adding RSI (Relative Strength Index)
    df['RSI'] = ta.rsi(df['close'], length=14)

    # Adding Bollinger Bands
    bbands = ta.bbands(df['close'], length=20, std=2)
    df = df.join(bbands)

    # Adding MACD (Moving Average Convergence Divergence)
    macd = ta.macd(df['close'], fast=12, slow=26, signal=9)
    df = df.join(macd)

    return df


# Process the API data
cleaned_df = process_data(time_series)
df_with_indicators = add_technical_indicators(cleaned_df)

def process_stock_data():
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype({'open': 'float', 'high': 'float', 'low': 'float', 'close': 'float', 'volume': 'int'})

    # Add technical indicators
    df['RSI'] = ta.rsi(df['close'], length=14)
    df = df.join(ta.bbands(df['close'], length=20, std=2))
    df = df.join(ta.macd(df['close'], fast=12, slow=26, signal=9))

    return df

@app.route('/data')
def data():
    df = process_stock_data()
    return jsonify(df.to_dict(orient='list'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


