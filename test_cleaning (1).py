import pandas as pd
from cleaning import clean_orders, clean_games

def make_raw():
    return pd.DataFrame({
        "order_id": [1, 2, 2, 3, 4, 5],
        "customer": ["Amit", "Riya", "Riya", None, "Karan", "Neha"],
        "amount": ["500", "700", "700", "abc", "1200", None],
        "city": ["Jaipur", "Delhi", "Delhi", "Jaipur", "jaipur", "Mumbai"],
    })

def make_raw_games():
    return pd.DataFrame({
        "Name": ["Halo", "Halo", None, "Mario"],
        "Platform": ["Xbox", "Xbox", "PS4", "Wii"],
        "Year_of_Release": [2001.0, 2001.0, 2010.0, None],
        "Genre": ["Shooter", "Shooter", "Action", "Platform"],
        "User_Score": ["8.5", "8.5", "7", "tbd"],
    })

def test_duplicates_removed():
    assert clean_orders(make_raw())["order_id"].is_unique

def test_no_missing_amounts():
    assert clean_orders(make_raw())["amount"].isna().sum() == 0

def test_city_names_standardised():
    assert set(clean_orders(make_raw())["city"]) == {"Jaipur", "Delhi", "Mumbai"}

def test_filled_amounts_are_flagged():
    assert clean_orders(make_raw())["amount_filled"].sum() == 2

def test_missing_customer_becomes_unknown():
    assert "Unknown" in clean_orders(make_raw())["customer"].values

def test_games_missing_name_dropped():
    assert clean_games(make_raw_games())["Name"].notna().all()

def test_games_duplicates_removed():
    assert len(clean_games(make_raw_games())) == 2

def test_games_tbd_becomes_missing():
    assert clean_games(make_raw_games())["User_Score"].isna().sum() == 1
