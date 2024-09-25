import pandas as pd


# Function to process the data

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
