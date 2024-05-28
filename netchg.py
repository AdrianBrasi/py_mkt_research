# Create a df column of net chg in price open->close for each day
def price_chg_intraday_column(df):
    if df is None:
        raise ValueError("Enter the correct df")

    df['intraday_chg'] = df['close'] - df['open']


# Create a df column of rolling net chg in price close->close for x days
def price_chg_column(df, days):
    if df is None:
        raise ValueError("Enter the correct df")

    if days <= 0:
        raise ValueError("'days' should be a positive integer")

    newColumn = f'trailing {days}d chg'

    df[newColumn] = df['close'] - df['close'].shift(days)


# Print one line to the console that tells you the
# median close->close chg for x days
def price_chg_median(df, days, flag, precision):
    if df is None:
        raise ValueError("Enter the correct df")

    if days <= 0:
        raise ValueError("'days' should be a positive integer")

    if flag not in [-1, 0, 1]:
        raise ValueError(" 'flag' should be 0 for all,"
                         " -1 for negative values, and 1 for positive values")

    if precision <= 0:
        raise ValueError("Decimal point precision should be => 1")

    change = df['close'] - df['close'].shift(days)

    if flag == 0:
        median = change.median().round(precision)
        print(f'Median {days} day return: {median}')

    if flag == 1:
        median = (change[change > 0]).median().round(precision)
        print(f'Median {days} day positive return: {median}')

    if flag == -1:
        median = (change[change < 0]).median().round(precision)
        print(f'Median {days} day negative return: {median}')


