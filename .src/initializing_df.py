# initiallizing_df.py
# Load data
import pandas as pd
# Load the dataset
def load_data():
    df = pd.read_csv('synthetic_financial_data.csv')
    
    df["transaction_time"] = pd.to_datetime(df["transaction_time"])
    df["hour"] = df["transaction_time"].dt.hour

    return df