## DERIVITAVES MARKET DATA: USE AT YOUR OWN RISK ##

# This project is starting to feel like it will
# eventually mutate into an all-encompassing market
# research library that can handle intra-day data,
# any CSV, and maybe an API or two. It could possibly
# have a nice comfy GUI with dropdown menus. #

# At this current time I am exclusively using it to
# study the S&P500 Volatility Index daily OHLC data #

import os
import pandas as pd
import matplotlib.pyplot as plt

from modules import (checks,
                     price_distribution,
                     netchg)

# Make filepath machine-independent
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')
filepath = os.path.join(data_dir, 'vix.csv')

# Pandas dataframe
df = pd.read_csv(filepath)
checks.verify_df(df)
checks.prepare_df(df)

# Flags for all functions that take 'flag' argument. These are
# global variables that will be used in multiple modules #
all_flag = 0  # pass to calculate whole series
up_flag = 1  # pass to calculate only positive values
down_flag = -1  # pass to calculate only negative values

# CALL FUNCTIONS BELOW THIS LINE #

# Quick examples of how to use some functions
netchg.price_chg_column(df, 1)
x = price_distribution.calculate_quantiles(df, 0.75)
y = price_distribution.calculate_quantiles(df, 0.25)
z = netchg.price_chg_median(df, 20, 0, 3)
print("Third Quartile (whole dataset): ", x)
print("First Quartile (whole dataset): ", y)
print("Median 1d change for past 20 days: ", z)
print(df.tail(20))

