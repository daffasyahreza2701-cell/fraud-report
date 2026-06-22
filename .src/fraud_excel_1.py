import pandas as pd
from initializing_df import load_data

df = load_data()

mostfraud_card = df.groupby('card_type')['is_fraudulent'].mean().sort_values(ascending=False)

amount_compare = df.groupby('is_fraudulent')['amount'].describe()

mostfraud_customer = df.groupby('customer_id')['is_fraudulent'].sum().sort_values(ascending=False)

compare_all = df.groupby('is_fraudulent')['amount'].agg(['count', 'mean', 'median', 'sum'])

mostfraud_location = df.groupby('location')['is_fraudulent'].sum().sort_values(ascending=False)

mostfraud_age = df.groupby('customer_age')['is_fraudulent'].sum().sort_values(ascending=False)

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

with pd.ExcelWriter("fraud_report.xlsx") as writer:
    city_analysis.to_excel(writer, sheet_name="City Analysis")
    category_analysis.to_excel(writer, sheet_name="Fraud Category Analysis")
    mostfraud_card.to_excel(writer, sheet_name="Fraud Card Types")
    amount_compare.to_excel(writer, sheet_name="Transaction Comparison")
    mostfraud_customer.to_excel(writer, sheet_name="Most Fraudulent Customers")
    compare_all.to_excel(writer, sheet_name="Comparison of Fraudulent and Legitimate Transactions")
    mostfraud_location.to_excel(writer, sheet_name="Most Fraudulent Locations")
    mostfraud_age.to_excel(writer, sheet_name="Most Fraudulent Ages")