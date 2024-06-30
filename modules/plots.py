import pandas as pd
import matplotlib.pyplot as plt
from modules import netchg


# Takes in two dataframes and slices the longer one to make sure that the
# dataframes being compared are of equal length. It then proceeds to plot
# the comparison of both instruments The 3rd and 4th arguments control the
# granularity of the chart. If you have 20 years of data, you probably don't
# need a daily chart. The 3rd arg,'days_threshold_to_show_weekly_chart
# is set to a default value of 1000 days. The 4th arg, is the threshold for
# a monthly chart. But you can change the values if you please. If you want
# to cook your CPU by plotting 5000 days, that's up to you... #
def compare_two_instruments(df1: pd.DataFrame,
                            df2: pd.DataFrame,
                            days_threshold_to_show_weekly_chart: int = 1000,
                            days_threshold_to_show_monthly_chart: int = 2500):
    if df1 is None:
        raise ValueError("First dataframe is invalid")
    if df2 is None:
        raise ValueError("Second dataframe is invalid")

    df1.set_index('time', inplace=True)
    df2.set_index('time', inplace=True)

    common_dates = df1.index.intersection(df2.index)

    df1 = df1.loc[common_dates]
    df2 = df2.loc[common_dates]

    df1.index = pd.to_datetime(df1.index)
    df2.index = pd.to_datetime(df2.index)

    w_min = days_threshold_to_show_weekly_chart
    w_max = days_threshold_to_show_weekly_chart - 1
    m_min = days_threshold_to_show_monthly_chart

    plt.figure(figsize=(20,20))
    if w_min <= len(df1) <= w_max:
        df1_weekly = df1.resample('5D').last()
        df2_weekly = df2.resample('5D').last()
        plt.plot(df1_weekly.index, df1_weekly['close'], label=f'{df1}', color='blue')
        plt.plot(df2_weekly.index, df2_weekly['close'], label=f'{df2}', color='red')
    elif len(df1) > m_min:
        df1_monthly = df1.resample('21D').last()
        df2_monthly = df2.resample('21D').last()
        plt.plot(df1_monthly.index, df1_monthly['close'], label=f'{df1}', color='blue')
        plt.plot(df2_monthly.index, df2_monthly['close'], label=f'{df2}', color='red')
    else:
        plt.plot(df1.index, df1['close'], label=f'{df1}', color='blue')
        plt.plot(df2.index, df2['close'], label=f'{df2}', color='red')

    # Return of whole dataset
    df1_return = netchg.calc_return(df1)
    df2_return = netchg.calc_return(df2)
    df1_return_text = f'pct chg of df1: {df1_return:.2f}%'
    df2_return_text = f'pct chg of df2: {df2_return:.2f}%'

    box = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    ax = plt.gca()
    ax.text(0.05, 0.95, df1_return_text + '\n' + df2_return_text,
            transform=ax.transAxes, fontsize=30, verticalalignment='top', bbox=box)

    plt.tight_layout()
    plt.show()


# This simply plots a histogram of closing prices for however many days
# you want. This is not great for stocks that tend to have upward price
# discovery over time. It is better suited for things like VIX, economic
# data, and interest rates that tend to consistently fall into a range. #
def plot_distribution(df: pd.DataFrame, days_back: int=1, all_days=False):
    if df is None:
        raise ValueError("Enter the correct df")
    if days_back < 1:
        raise ValueError("Days back should be a positive integer")

    plt.figure(figsize=(20,20))

    if all_days:
        plt.hist(df['close'], bins='auto', color='#a9b1d6')
        plt.title('All days in dataset')
    else:
        plt.hist(df['close'].tail(days_back), bins='auto', color='#a9b1d6')
        plt.title(f'Last {days_back} days in dataset')

    plt.grid(color='#292e42')
    plt.gca().set_facecolor('#1f2335')
    plt.xlabel('Close values', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.tight_layout()
    plt.show()