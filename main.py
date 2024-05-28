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

import os
import pandas as pd
import matplotlib.pyplot as plt

import checks
import netchg

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

netchg.price_chg_median(df, 30, 0, 4)
netchg.price_chg_column(df, 10)

#print(df.head(20))
print(df.tail(20))
