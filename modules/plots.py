import pandas as pd
import matplotlib.pyplot as plt


# Takes in two dataframes and slices the longer one to make sure that the
# dataframes being compared are of equal length. It then proceeds to plot
# the comparison of both instruments #
def compare_two_instruments(df1: pd.DataFrame, df2: pd.DataFrame):
    if df1 is None:
        raise ValueError("First dataframe is invalid")
    if df2 is None:
        raise ValueError("Second dataframe is invalid")

    df1.set_index('time', inplace=True)
    df2.set_index('time', inplace=True)

    common_dates = df1.index.intersection(df2.index)

    df1 = df1.loc[common_dates]
    df2 = df2.loc[common_dates]

    plt.figure(figsize=(20,20))
    plt.plot(df1.index, df1['close'], label=f'{df1}', color='blue')
    plt.plot(df2.index, df2['close'], label=f'{df2}', color='red')

    plt.show()

