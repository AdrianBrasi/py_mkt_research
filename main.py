### DERIVITAVES MARKET DATA: USE AT YOUR OWN RISK ###

# INSTRUCTIONS: Open a daily chart on tradingview,
# scroll back as far as you want, then click 'export
# chart data' in the top right dropdown menu. Select
# ISO time. Move the .CSV to the 'data' subdirectory
# in this project. Do not adjust the column names #

# This project is starting to feel like it will
# eventually mutate into an all-encompassing market
# research library that can handle intra-day data
# from any Tradingview CSV. It could possibly
# have a nice comfy GUI with dropdown menus. #


import os
import pandas as pd
import matplotlib.pyplot as plt

from modules import (checks,
                     price_distribution,
                     netchg,
                     plots)

# Make filepath machine-independent
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

# Load all the .CSV files you want
ndx_csv = os.path.join(data_dir, 'ndx.csv')
spx_csv = os.path.join(data_dir, 'spx.csv')
vix_csv = os.path.join(data_dir, 'vix.csv')

# Create and clean pandas dataframe
ndx = pd.read_csv(ndx_csv)
spx = pd.read_csv(spx_csv)
vix = pd.read_csv(vix_csv)
checks.verify_df(ndx)
checks.prepare_df(ndx)
checks.verify_df(spx)
checks.prepare_df(spx)
checks.verify_df(vix)
checks.prepare_df(vix)

# Flags for all functions that take 'flag' argument. These are
# global variables that will be used in multiple modules #
all_flag = 0  # pass to calculate whole series
up_flag = 1  # pass to calculate only positive values
down_flag = -1  # pass to calculate only negative values

# CALL FUNCTIONS BELOW THIS LINE #

# plots.compare_two_instruments(spx, ndx)
plots.plot_distribution(vix, all_days=True)
