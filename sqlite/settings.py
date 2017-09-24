TRACK_TERMS = ["DACA", "#DACA", "daca", "#daca", "immigration rules"]
CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "DACA"

API_KEY = "#"

API_SECRET = "#"

ACCESS_KEY = "#"

ACCESS_SECRET = "#"


try:
    from private import *
except Exception:
    pass