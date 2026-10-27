import pandas as pd

def clean_orders(df):
    df = df.drop_duplicates()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["city"] = df["city"].str.strip().str.title()
    df["customer"] = df["customer"].fillna("Unknown")
    df["amount_filled"] = df["amount"].isna()
    df["amount"] = df["amount"].fillna(df["amount"].median())
    return df

def clean_games(df):
    df = df.copy()
    df = df.dropna(subset=["Name", "Genre"])
    df = df.drop_duplicates(subset=["Name", "Platform", "Year_of_Release"])
    df["User_Score"] = pd.to_numeric(df["User_Score"], errors="coerce")
    df["Year_of_Release"] = df["Year_of_Release"].astype("Int64")
    return df
