import pandas as pd

filepath = '~/projects/mktresearch/vix/data/vix.csv'
df = pd.read_csv(filepath)
df = df.drop_duplicates()

# Change ISO time to human-readable format
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.strftime('%Y %m %d')


# Net change in price
def calculateChgPrice(df, days):
    if days <= 0:
        raise ValueError("'days' should be a positive integer!")
    newColumn = f'{days}DayChg'
    df[newColumn] = df['close'] - df['close'].shift(days)


calculateChgPrice(df, 1)
calculateChgPrice(df, 5)
calculateChgPrice(df, 10)

#print(df.head(20))
print(df.tail(20))
