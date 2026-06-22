# fraud_analysis.py
from initiallizing_df import load_data
# Load the dataset
df = load_data()
# Display the first few rows of the dataset
print(df.head())
# Display the Column Names
print(df.columns)
# Dsiplay the data types of each column
print(df.dtypes)
# Check for missing Values
print(df.isnull().sum())
# Basic statistics
print(df.describe())
# basic info
print(df.info())
# data cleaning, first the duplicates and then the missing values
print(df.drop_duplicates())
print(df.dropna())
# checking the unique card types
print(df['card_type'].unique())
# checking the unique purchase categories
print(df['purchase_category'].unique())
# checking the unique locations
print(df['location'].unique())
# Which card type are the most used?
print(df['card_type'].value_counts())
# Which card type had the most amounts in transaction
print(df.groupby('card_type')['amount'].sum().sort_values(ascending=False))
# How common is fraudulent transactions?
print(df['is_fraudulent'].value_counts(normalize=True) * 100)
# Which card type has the most fraud done?
print(df.groupby('card_type')['is_fraudulent'].mean().sort_values(ascending=False))
# Are fraudulent transactions larger?
print(df.groupby('is_fraudulent')['amount'].describe())
# Which customer has the most fraudulent transactions?
print(df.groupby('customer_id')['is_fraudulent'].sum().sort_values(ascending=False))
# Compare fraudulent and legitimate transactions
print(df.groupby('is_fraudulent')['amount'].agg(['count', 'mean', 'median', 'sum']))
# Which card type has the minimum amount of fraud done?
print(df.groupby('card_type')['is_fraudulent'].sum().sort_values(ascending=True))
# What Place of transaction are usually the most fraud prominent?
print(df.groupby('location')['is_fraudulent'].sum().sort_values(ascending=False))
# What age does the most amount of fraud?
print(df.groupby('customer_age')['is_fraudulent'].sum().sort_values(ascending=False))
# What purchase category does have the most amount of fraud?
print(df.groupby('purchase_category')['is_fraudulent'].sum().sort_values(ascending=False))
# fraud rate
city_analysis = (
    df.groupby('location')['is_fraudulent']
    .agg(
        total_transactions = 'count',
        fraud_transactions = 'sum',
        fraud_rate = 'mean'
    )
)

city_analysis['fraud_rate'] *= 100

city_analysis.sort_values(by='fraud_rate', ascending=False)

print(city_analysis)

# purchase category fraud rate
category_analysis = (
    df.groupby('purchase_category')['is_fraudulent']
    .agg(
        total_transactions = 'count',
        fraud_transactions = 'sum',
        fraud_rate = 'mean'
    )
)
category_analysis['fraud_rate'] *= 100
category_analysis.sort_values(by='fraud_rate', ascending=False)
print(category_analysis)