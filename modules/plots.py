import pandas as pd
import matplotlib.pyplot as plt


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

    plt.show()

