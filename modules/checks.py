import warnings
import pandas as pd


# Call this before you do anything with your dataframes.
# If the warnings annoy you, delete or comment out the lines
# pertaining to 'optional_columns'. Furthermore, you can add
# required/optional columns as you please #
def verify_df(df: pd.DataFrame) -> None:
    if df is None or not isinstance(df, pd.DataFrame):
        raise TypeError("Invalid dataframe. Cannot perform operations. Check your .CSV")

    required_columns = ['open', 'high', 'low', 'close', 'time']

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f'Required column: {column} is missing')

    optional_columns = ['Volume', 'ATR']

    for column in optional_columns:
        if column not in df.columns:
            warnings.warn(f'Optional column: {column} is missing')


# Basic cleanup and change 'time' column from ISO time to human-readable format
# Just add your favorite pre-analysis adjustments to this function #
def prepare_df(df: pd.DataFrame):
    df = df.drop_duplicates(subset=['time'])
    df = df.dropna()
    pd.set_option('display.max_columns', None)
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.strftime('%Y %m %d')
    df['time'] = df['time'].astype(str)
