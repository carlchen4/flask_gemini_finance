import pandas as pd

def analyze_transactions(transactions):
    df = pd.DataFrame(transactions)
    spending_summary = df.groupby('category')['amount'].sum().to_dict()
    return spending_summary
