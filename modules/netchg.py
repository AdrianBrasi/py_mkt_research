import pandas as pd


# Create a df column of net chg in price open->close for each day
def price_chg_intraday_column(df: pd.DataFrame):
    if df is None:
        raise ValueError("Enter the correct df")

    df['intraday_chg'] = df['close'] - df['open']


# Create a df column of rolling net chg in price close->close for x days
def price_chg_column(df: pd.DataFrame, days: int):
    if df is None:
        raise ValueError("Enter the correct df")

    if days <= 0:
        raise ValueError("'days' should be a positive integer")

    newColumn = f'trailing {days}d chg'

    df[newColumn] = df['close'] - df['close'].shift(days)


# Print one line to the console that tells you the
# median close->close 1d chg for past x days
def price_chg_median(df: pd.DataFrame, days: int, flag: int, precision: int):
    if df is None:
        raise ValueError("Enter the correct df")

    if days <= 0:
        raise ValueError("'days' should be a positive integer")

    if flag not in [-1, 0, 1]:
        raise ValueError(" 'flag' should be 0 for all,"
                         " -1 for negative values, and 1 for positive values")

    if precision <= 0:
        raise ValueError("Decimal point precision should be => 1")

    one_day_change = df['close'] - df['close'].shift(1)

    change = one_day_change[days:]

    if flag == 0:
        data_to_calculate = change
    elif flag == 1:
        data_to_calculate = change[change > 0]
    else:
        data_to_calculate = change[change < 0]

    data_to_calculate = data_to_calculate.dropna()
    median = data_to_calculate.median().round(precision)

    return median


def chg_from_date_to_date(df: pd.DataFrame, start: str, end: str, pct=False):
    if df is None:
        raise ValueError("Enter vaild df")

    start_index = df[df['time'] == start].index[0]
    end_index = df[df['time'] == end].index[0]

    if pct:
        chg = (df.loc[end_index, 'close'] - df.loc[start_index, 'close']) / df.loc[start_index, 'close'] * 100
    else:
        chg = df.loc[end_index, 'close'] - df.loc[start_index, 'close']

    return chg.round(3)

