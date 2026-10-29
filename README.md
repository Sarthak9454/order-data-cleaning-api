# Data Cleaning Pipeline & Summary API

A Python pipeline that cleans messy order data, answers business questions with SQL, and serves a Flask API that adds an LLM-written summary.

## What it does
- Cleans duplicates, missing values, wrong data types and inconsistent text with Pandas
- Flags imputed values instead of hiding them
- Loads clean data into SQLite and queries it with GROUP BY, HAVING and LEFT JOIN
- Flask API with /clean and /clean-and-summarize endpoints
- Calls the Gemini API with a timeout and a plain-Python fallback; numbers are computed in code and the model only phrases them
- Also cleans a 16,700-row video game sales dataset

## Tests
pytest, 8 tests (run with `pytest -v`)

## Tech
Python, Pandas, SQLite, Flask, pytest, Gemini API (Google Colab)

## Notes
The API was tested with Flask's test client and run as a live server inside Colab. It is not deployed.

Dataset: https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings
