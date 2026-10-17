import pandas as pd
from cleaning import clean_orders

def make_raw():
    return pd.DataFrame({
        "order_id": [1, 2, 2, 3, 4, 5],
        "customer": ["Amit", "Riya", "Riya", None, "Karan", "Neha"],
        "amount": ["500", "700", "700", "abc", "1200", None],
        "city": ["Jaipur", "Delhi", "Delhi", "Jaipur", "jaipur", "Mumbai"],
    })

def test_duplicates_removed():
    cleaned = clean_orders(make_raw())
    assert cleaned["order_id"].is_unique

def test_no_missing_amounts():
    cleaned = clean_orders(make_raw())
    assert cleaned["amount"].isna().sum() == 0

def test_city_names_standardised():
    cleaned = clean_orders(make_raw())
    assert set(cleaned["city"]) == {"Jaipur", "Delhi", "Mumbai"}

def test_filled_amounts_are_flagged():
    cleaned = clean_orders(make_raw())
    assert cleaned["amount_filled"].sum() == 2

def test_missing_customer_becomes_unknown():
    cleaned = clean_orders(make_raw())
    assert "Unknown" in cleaned["customer"].values
