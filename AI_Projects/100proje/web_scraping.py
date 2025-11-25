import numpy as np
import pandas as pd
import requests

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page {response.status_code}")
        return None

print(fetch_page("https://finance.yahoo.com/quote/AAPL/"))