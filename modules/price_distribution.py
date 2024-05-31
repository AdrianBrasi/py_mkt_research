# These functions appear redundant, but I want to be able to
# call them separately and pass their return values into other
# equations and matplotlilb graphs #

import pandas as pd


def calculate_median_close(df: pd.DataFrame, days_back: int, all_days=False):
    if df is None:
        raise ValueError("Enter the correct df")
    if days_back < 1:
        raise ValueError("Days back should be a positive integer")

    if all_days:
        day_range = df['close']
    else:
        day_range = df.loc[max(0, len(df) - days_back):, 'close']

    median_close = day_range.median().round(4)

    return median_close


def calculate_mean_close(df: pd.DataFrame, days_back: int, all_days=False):
    if df is None:
        raise ValueError("Enter the correct df")
    if days_back < 1:
        raise ValueError("Days back should be a positive integer")

    if all_days:
        day_range = df['close']
    else:
        day_range = df.loc[max(0, len(df) - days_back):, 'close']

    mean_close = day_range.mode().round(4)

    return mean_close


def calculate_mode_close(df: pd.DataFrame, days_back: int, all_days=False):
    if df is None:
        raise ValueError("Enter the correct df")
    if days_back < 1:
        raise ValueError("Days back should be a positive integer")

    if all_days:
        day_range = df['close']
    else:
        day_range = df.loc[max(0, len(df) - days_back):, 'close']

    mode_close = day_range.mode().round(4)

    return mode_close


def calculate_quantiles(df: pd.DataFrame, qtile: float):
    if df is None:
        raise ValueError("Enter the correct df")
    if (qtile > 1) or (qtile < 0):
        raise ValueError("Quantile value must be a float between 0.00 and 1.00")
    else:
        q: float = df['close'].quantile(qtile)
        return q
