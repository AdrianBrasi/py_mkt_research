import pandas as pd


def verify_df(df):
    if df is None:
        raise TypeError("Invalid dataframe. Cannot perform operations. Check your .CSV")
    else:
        if 'open' not in df.columns:
            raise ValueError("'open' does not exist. Check your data!")
        if 'close' not in df.columns:
            raise ValueError("'close' does not exist. Check your data!")
        if 'low' not in df.columns:
            raise ValueError("'low' does not exist. Check your data!")
        if 'high' not in df.columns:
            raise ValueError("'high' does not exist. Check your data!")
        if 'time' not in df.columns:
            raise ValueError("'time' does not exist. You may have 'date' instead of 'time'")
        else:
            return None


# Basic cleanup and change 'time' column from ISO time to human-readable format
# Just add your favorite pre-analysis adjustments to this function #
def prepare_df(df):
    df = df.drop_duplicates(subset=['time'])
    df = df.dropna()
    pd.set_option('display.max_columns', None)
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.strftime('%Y %m %d')
