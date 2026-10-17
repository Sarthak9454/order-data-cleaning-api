import pandas as pd

def clean_orders(df):
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["city"] = df["city"].str.strip().str.title()
    df["customer"] = df["customer"].fillna("Unknown")
    df["amount_filled"] = df["amount"].isna()
    df["amount"] = df["amount"].fillna(df["amount"].median())
    return df
