## DERIVITAVES MARKET DATA: USE AT YOUR OWN RISK ##

# This is currently just some math in a .py file,
# but it will eventually be an all-encompassing study
# of one of the most important financial instruments
# in the world: THE S&P500 VOLATILITY INDEX #

# The endgoal: A comfy GUI where you plug in a .CSV,
# and chose what you want to know in a series of drop-down
# menus. I will consider the possibility hooking this up to
# different APIs. Whether this stays a standalone application,
# or a website remains to be seen. I am unsure about the legal
# implications of mixing FOSS with financial market data... #

#TODO: Why is the 'precision' argument in the 'calculate_medians' function
# capping the decimal place to 2? #

import os
import pandas as pd

# Make filepath machine-independent
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')
filepath = os.path.join(data_dir, 'vix.csv')

# Pandas dataframe
df = pd.read_csv(filepath)
df = df.drop_duplicates()
pd.set_option('display.max_columns', None)

# Change ISO time to human-readable format
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.strftime('%Y %m %d')

# Net change in price open->close for each day
df['intradayChg'] = df['close'] - df['open']


# Net change in price close->close for 'x' days
def calculate_chg_price(df, days):
    if df is None:
        raise ValueError("Enter the correct df")
    if days <= 0:
        raise ValueError("'days' should be a positive integer")
    newColumn = f'{days}DayChg'
    df[newColumn] = df['close'] - df['close'].shift(days)


m_flag = 0  # pass to calculate whole series
up_flag = 1  # pass to calculate only positive values
down_flag = -1  # pass to calculate only negative values


def calculate_medians(df, days, flag, precision):
    if df is None:
        raise ValueError("Enter the correct df")

    if days <= 0:
        raise ValueError("'days' should be a positive integer")

    if flag not in [-1, 0, 1]:
        raise ValueError(" 'flag' should be 0 for all,"
                         " -1 for negative values, and 1 for positive values")

    change = df['close'] - df['close'].shift(days)

    if flag == 0:
        median = change.median().round(precision)
        return f'Median {days} day return: {median}'

    if flag == 1:
        median = (change[change > 0]).median().round(precision)
        return f'Median {days} day positive return: {median}'

    if flag == -1:
        median = (change[change < 0]).median().round(precision)
        return f'Median {days} day negative return: {median}'


print(calculate_medians(df, 5, 0, 5))

calculate_chg_price(df, 1)
calculate_chg_price(df, 5)
calculate_chg_price(df, 10)

#print(df.head(20))
print(df.tail(20))


